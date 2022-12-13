import json
import csv

"""Извлечение данных из файла json"""

with open('data.json', 'r') as file:
    data = json.load(file)

"""Извлечение информации в csv файл"""
with open('data.csv', 'w') as csvfile:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in data:
        writer.writerow(i)
