from instascrape import Reel
from  datetime import time

'''# session id
SESSIONID = "Paste session Id Here"

# Header with session id
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    "cookie": f'sessionid={SESSIONID};'
}

# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(
    'https://www.instagram.com/reel/CKWDdesgv2l/?utm_source=ig_web_copy_link')

# Using  scrape function and passing the headers
insta_reel.scrape(headers=headers)

# Giving path where we want to download reel to the
# download function
# date = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
date = datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
timestr = time.strftime("%Y%m%d_%H%M%S")
insta_reel.download(f"reel_{date}.mp4")
# insta_reel.download(f"D:/reel_{date}.mp4")
# insta_reel.
# printing success Message
# print(timestr)
print('Downloaded Successfully.')'''


def download(video_link):

    try:
        if(video_link):
            SESSIONID = "Paste session Id Here"
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
            Safari/537.36 Edg/79.0.309.43",
            "cookie": f'sessionid={SESSIONID};'
            }

            insta_reel = Reel(video_link)
            # print(insta_reel)

            # Using  scrape function and passing the headers
            insta_reel.scrape(headers=headers)

            # Giving path where we want to download reel to the
            # download function
            date = datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p")
            insta_reel.download(f"reel_{date}.mp4")
            # printing success Message
            print('Downloaded Successfully.')
        else:
            pass
    except Exception as e:
        print('Enter valid Link')

data = input('Enter reels video link with https: ')


download(data)

# print(demo)
