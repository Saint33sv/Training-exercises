import requests
from easygui import *
from random import randrange
import os

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36',
    'accept': '*/*'
}
payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
payload2 = {'method': 'getQuote', 'format': 'json', 'lang': 'en'}


def pars(params):
    url = 'http://api.forismatic.com/api/1.0/'
    r = requests.get(url, headers=HEADERS, params=params)
    msgbox(msg=f"{r.json()['quoteText']}\n{r.json()['quoteAuthor']}", title='Цитаты великих людей')



links_cats = ['/cat', '/cat/says/text', '/cat/says/something?color=color', '/cat?filter=filter']
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36',
    'accept': '*/*'
}


def cats_parse():
        url = f'https://cataas.com{links_cats[randrange(len(links_cats))]}'
        r = requests.get(url, headers=head)
        with open('cat.jpeg', 'wb') as file:
            file.write(r.content)
        os.system('cat.jpeg')


if __name__ == '__main__':
    language_button = ['Русский', 'Английский', 'Просто кот']
    language = [payload, payload2]
    while True:
        rec = buttonbox(msg='Выберите язык!', title='Цитаты великих людей', choices=language_button)
        if rec is None:
            break
        elif rec == language_button[2]:
            cats_parse()
        else:
            pars(language[language_button.index(rec)])
