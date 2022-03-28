# facebook-group-photos-scrapper

Downloads photos posted in public facebook group.

## How to use:

### Install requirements

`pip install -r requirements.txt`

### Get facebook group id from its url

`https://www.facebook.com/groups/{group_id}`

### Export facebook cookies file using chrome extension

https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid
And save them as a `facebook.com_cookies.txt` file in projects root directory.

### Run script

`python scrap_photos.py {group_id}`
For example:
`python scrap_photos.py 461241481043213`
Script will now attempt to download all photos posted in this group into `img` directory.
