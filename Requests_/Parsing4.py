import requests
from bs4 import BeautifulSoup
import json
import csv
"""Парсинг данных из интернет магазина и запись в двух форматах json и csv"""

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36',
    'accept': '*/*'
}

data = []


def parse(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('article', class_='item-list group')
    for item in items:
        item: BeautifulSoup
        name = item.find('a', class_='name-big').text.strip()
        link = 'https://www.maxidom.ru' + item.find('a', class_='name-big')['href']
        price = item.find('span', class_='price-list').find('span').text.strip()[:-2]  # срез убирает два не нужных элемента после цифр
        d = {
            'name': name,
            'price': price,
            'link': link
        }
        data.append(d)


if __name__ == '__main__':
    for i in range(1, 35):
        URL = f'https://www.maxidom.ru/catalog/kruzhki/?amount=12&PAGEN_3={i}'
        parse(URL)
        print(f'Спарсили {i} страниц из 34')

    with open('parsdata.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    with open('parsdata.csv', 'w') as file:
        fieldnames = ['name', 'price', 'link']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)


