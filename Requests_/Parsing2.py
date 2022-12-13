import csv
import requests
from bs4 import BeautifulSoup
import json
"""Парсинг каталога цен и нименования продуктов сохранение данных в json"""


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/101.0.4951.67 Mobile Safari/537.36',
    'Accept': '*/*'
}
data = []


def parse(url):
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find('div', class_='catalog catalog-in visible').find_all('li')
        for item in items:
            name = item.find('a', class_='name-product').text
            price = item.find('div', class_='price').text.strip()
            d = {
                'name': name,
                'price': price
            }
            data.append(d)


for i in range(1, 7):
    url = f'https://www.muztang.ru/gitary-i-aksessuary/gitary/akusticheskie-gitary/?PAGEN_1={i}'
    parse(url)
print(data)


with open('data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


with open('data.csv', 'w') as filecsv:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(filecsv, fieldnames=fieldnames)
    writer.writeheader()
    for elem in data:
        writer.writerow(elem)


