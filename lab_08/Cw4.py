import csv
from collections import namedtuple

with open('zamowienia.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=';')

    names = next(reader)
    for i in range(len(names)):
        names[i] = names[i].replace(' ', '_')

    Orders = namedtuple('Orders', names)
    namedtuple_list = []

    for i in range(10):
        order = Orders(*next(reader))
        namedtuple_list.append(order)

print(namedtuple_list)
