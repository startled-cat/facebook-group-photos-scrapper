from facebook_scraper import get_posts
import requests
import shutil
import os
import sys

OUTPUT_DIR = "img"
FACEBOOK_COOKIE_FILE = "facebook.com_cookies.txt"
if not os.path.exists(FACEBOOK_COOKIE_FILE):
    print(
        f"Error: Facebook cookie file ({FACEBOOK_COOKIE_FILE}) does not exist\nTo export your facebook cookies use this chrome extension: https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid")
    exit(1)
if len(sys.argv) <= 1:
    print(
        f"Error: Missing argument: Facebook group id")
    exit(1)
FACEBOOK_GROUP_ID = sys.argv[1]  # '461241481043213'
print(f"Facebook group id = {FACEBOOK_GROUP_ID}")

posts = get_posts(group=FACEBOOK_GROUP_ID, cookies=FACEBOOK_COOKIE_FILE)
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

for post in posts:
    for image in post["images"]:
        file_name = image.split('/')[-1].split('?')[0]
        if len(file_name) == 0:
            file_name = image.split("/")[-1].split("&")[0][6:] + ".jpg"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        print(f"{file_path=}")
        if not os.path.exists(file_path):
            r = requests.get(image, stream=True)
            if r.status_code == 200:
                with open(file_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    print(f"Photo downloaded, {file_path}")
        else:
            print(f"Photo already exists, {file_path}")
