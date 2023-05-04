import csv
from datetime import datetime


def clean_utarg(utarg):
    return utarg.replace('z', '').replace(',', '.').replace(' ', '')


def clean_data_zamowienia(data):
    return datetime.strptime(data, '%d.%m.%Y').strftime('%Y-%m-%d')


with open('zamowienia.csv', 'r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=';')
    columns = reader.fieldnames

    lines = list(
        map(
            lambda x: {
                **x,
                'Utarg': clean_utarg(x['Utarg']),
                'Data zamowienia': clean_data_zamowienia(x['Data zamowienia']),
            },
            reader,
        )
    )

    pl = list(filter(lambda x: x['Kraj'] == 'Polska', lines))
    de = list(filter(lambda x: x['Kraj'] != 'Polska', lines))


with open('zamowienia_polska.csv', 'w') as file_pl:
    writer = csv.DictWriter(file_pl, fieldnames=columns)
    writer.writeheader()
    writer.writerows(pl)

with open('zamowienia_niemcy.csv', 'w') as file_de:
    writer = csv.DictWriter(file_de, fieldnames=columns)
    writer.writeheader()
    writer.writerows(de)
