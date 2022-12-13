import requests
"""Cкачивание картинки(не крупного файла) двумя способами"""
url = 'https://image.shutterstock.com/image-photo/skeptic-surprised-cat-thinking-dont-600w-1905929728.jpg'
headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
# r = requests.get(url, headers=headers, stream=True)
#
# with open('1.jpg', 'wb') as fd:
#     for i in r.iter_content(chunk_size=1024 * 10):
#         fd.write(i)
#         print('Write i 10Kb')
#

r = requests.get(url, headers=headers)

with open('2.jpg', 'wb') as fd:
    fd.write(r.content)
