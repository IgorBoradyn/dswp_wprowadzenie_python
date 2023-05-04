import csv
from datetime import datetime

pl = list(dict())
de = list(dict())

with open('zamowienia.csv', 'r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=';')
    columns = reader.fieldnames
    for line in reader:
        line['Utarg'] = line['Utarg'].replace('z', '')
        line['Utarg'] = line['Utarg'].replace(',', '.')
        line['Utarg'] = line['Utarg'].replace(' ', '')
        line['Data zamowienia'] = datetime.strptime(line['Data zamowienia'], '%d.%m.%Y').strftime('%Y-%m-%d')

        if line['Kraj'] == 'Polska':
            pl.append(line)
        else:
            de.append(line)


with open('zamowienia_polska.csv', 'w') as file_pl:
    writer = csv.DictWriter(file_pl, fieldnames=columns)

    writer.writeheader()
    for line in pl:
        writer.writerow(line)

with open('zamowienia_niemcy.csv', 'w') as file_de:
    writer = csv.DictWriter(file_de, fieldnames=columns)

    writer.writeheader()
    for line in de:
        writer.writerow(line)
