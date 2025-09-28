[app]
title = Kivy Test
package.name = kivytest
package.domain = org.example
source.dir = src
source.include_exts = py,png,jpg,kv,atlas,ttf,xml
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 28
android.ndk = 25b
android.ndk_api = 28
android.gradle_dependencies = 
# e.g. com.android.support:appcompat-v7:28.0.0

# This ensures no private data dump (since we’re not using poetry/setup.py)
ignore_setup_py = 1

# Permissions (add as needed)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icon & Presplash (place your images in project root)
#icon.filename = %(source.dir)s/icon.png
#presplash.filename = %(source.dir)s/presplash.png

# Entry point (your main Python file)
entrypoint = src//main.py

# Copy libs directly (needed for modern Android builds)
android.copy_libs = 1


[buildozer]
log_level = 2
warn_on_root = 1

# To cache in CI/CD
bin_dir = bin
build_dir = .buildozer

# Enable modern AndroidX support
enable_androidx = 1
