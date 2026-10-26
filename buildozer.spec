[app]

# (str) Title of your application
title = Gold Price Tracker

# (str) Package name
package.name = goldtracker

# (str) Package domain (needed for android packaging)
package.domain = org.gold

# (str) Source files where the let's go app lives
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# تأكد من تضمين جميع المكتبات التي يستوردها كودك
requirements = python3,kivy,certifi,urllib3

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether you accept the Android SDK License
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
