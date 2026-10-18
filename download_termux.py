#!/usr/bin/env python3
"""
Official Termux APK downloader
Downloads the latest universal APK for Android 7+ from termux/termux-app releases
"""

import requests
import sys
import os

def get_latest_apk():
    url = "https://api.github.com/repos/termux/termux-app/releases/latest"
    print("Latest release খুঁজছি...")
    
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        
        for asset in data.get("assets", []):
            name = asset["name"]
            if "apt-android-7" in name and "universal" in name and name.endswith(".apk"):
                download_url = asset["browser_download_url"]
                filename = name
                print(f"পাওয়া গেছে: {filename}")
                print(f"ডাউনলোড শুরু হচ্ছে...")
                
                with requests.get(download_url, stream=True) as resp:
                    resp.raise_for_status()
                    with open(filename, "wb") as f:
                        for chunk in resp.iter_content(chunk_size=8192):
                            f.write(chunk)
                
                print(f"\n✅ সফল! ফাইল সেভ হয়েছে: {filename}")
                print(f"সাইজ: {os.path.getsize(filename) / (1024*1024):.1f} MB")
                return
        
        print("কোনো উপযুক্ত APK পাওয়া যায়নি।")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_latest_apk()
