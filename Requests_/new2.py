import requests
"""Скачивание видео с помощью Python"""

url = 'https://ak.picdn.net/shutterstock/videos/1053115304/preview/stock-footage-family-vacation-travel-rv-holiday-trip-in-motorhome-caravan-car-vacation-beautiful-nature-norway.webm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

r = requests.get(url, headers=headers, stream=True)


with open('webvideo01.webm', 'wb') as wv:
    for i in r.iter_content(chunk_size=1024 * 100):
        wv.write(i)
        print('Write i 100Kb')
