import requests
import fake_useragent


ua = fake_useragent.UserAgent()

headers = {
    'User-Agent': ua.ie
}
# r = requests.get('https://httpbin.org/get', headers=headers)


# print(r.headers)
# print(r.content)
# print(r.text)
# print(r.json())

data = {
    'custname': 'Vasia',
    'custtel': '990-234-45-75',
    'custemail': 'Vasia@emil.com',
    'comments': 'fuck of...'
}

r = requests.post('https://httpbin.org/post', headers=headers, data=data)

print(r.text)
