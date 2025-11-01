[app]
title = DL6-OxygenFight
package.name = craft.soul.dl6
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = image/*
version = 12.28
requirements = python==3.9,kivy==2.2.1,plyer,cython,kivymd,https://github.com/kivymd/KivyMD/archive/master.zip
orientation = portrait
entrypoint=main.py
android.accept_sdk_license = True
android.allow_api_min = 21
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.gradle_download = https://services.gradle.org/distributions/gradle-7.5-all.zip
exclude_patterns = **/test/*, **/tests/*
