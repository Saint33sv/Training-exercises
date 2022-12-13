import requests
from bs4 import BeautifulSoup
import json
import csv

HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36',
        'accept': '*/*'
    }
data = []
link_data = []


def pars():

    url = 'https://kasta.ua/market/muzhskie-krossovki-i-kedy~brand_adidas/'
    r = requests.get(url, headers=HEADERS)
    r.encoding = 'url-8'  # Принудительно выставляет кодировку в тех случаях когда не работает автоматически
    soup = BeautifulSoup(r.text, 'html.parser')
    it = soup.find('div', class_='list-render')
    items = it.find_all('article', class_='p__item group')
    for item in items:
        item: BeautifulSoup
        name = item.find('header', class_='p__info_name').text
        not_price = item.find('span', class_='product_item__new-cost').text.strip()[:-4]
        link = item.find('img', class_='lazy nojs-hide aspect-inner')['data-src']
        description = item.find('span', class_='wrapper-properties').text.replace('/', '').replace('\n', ' ').\
            replace('\t', ' ').replace('\u2015', '')
        list = []
        for i in not_price:
            list.append(i)
        list.pop(1)
        price = ''.join(list)

        link_data.append(link)
        d = {
            'name': name,
            'price': price,
            'link': link,
            'description': description
        }
        data.append(d)
    # print(data)


if __name__ == '__main__':
    pars()
    for i in range(len(link_data)):
        r = requests.get(link_data[i], headers=HEADERS)
        with open(f'Photo/photo{i}.jpeg', 'wb') as file:
            file.write(r.content)
    with open('pars5.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    with open('pars.csv', 'w') as file:
        fieldnames = ['name', 'price', 'link', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(i)

