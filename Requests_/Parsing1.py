import requests
import fake_useragent
from bs4 import BeautifulSoup
"""Парсинг данных с сайта адресс и время работы магазина"""

url = 'https://www.muztang.ru/gitary-i-aksessuary/chekhly-i-keysy-dlya-gitar/keys-dlya-bas-gitar/'
us = fake_useragent.UserAgent()

headers = {
    'User-Agent': us.random,
    'Accept': '*/*'
}

r = requests.get(url=url, headers=headers)

if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    adres = soup.find('address', class_='address').text.strip()
    time = soup.find('div', class_='time').find('span').text
    print(adres)
    print(time)
