[app]

# (str) Title of your application
title = Twinkle

# (str) Package name
package.name = twinkle

# (str) Package domain (unique domain for your app)
package.domain = com.example.twinklebeta

# (str) Source code where your main.py is located
source.dir = .

# (str) The main entry point of the application
source.include_exts = py,png,jpg,kv,atlas

# (list) Permissions required for the app
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO

# Fullscreen setting
fullscreen = 1

# (str) Icon of the application
icon.filename = icon.png

# (int) Target Android API, Android 13
android.api = 33

# (int) Minimum API level (Android 5.0 and above)
android.minapi = 21

# (str) Supported orientations
#orientation = sensor

# (list) Requirements
requirements = python3, kivy, ftplib, watchdog

# (bool) Indicate if the application is a game
is_game = 0

# (str) Presplash screen
#presplash.filename = presplash.png

# (str) Presplash background color
presplash.color = #ffffff

# (list) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# Enable storage access for app-specific storage
android.allow_backup = 1

# Android-specific configurations for performance
android.hardwareAccelerated = true
android.preserve_sdcard = true

# (str) Path to a custom Java class
android.entrypoint = org.kivy.android.PythonActivity

# Application metadata
version = 1.0
android.debug = 1
android.compile_options = -source 1.8 -target 1.8

# Enable the immersive full-screen experience
android.meta-data.fullscreen_mode = immersive
