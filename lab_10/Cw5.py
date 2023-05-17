import csv
from datetime import datetime


def change_date(filename, date_index, src, dst):
    with open(filename, 'r') as f:
        with open(f'new_{filename}', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            reader = csv.reader(f, delimiter=';')

            col_names = next(reader)
            writer.writerow(col_names)

            for row in reader:
                date = datetime.strptime(row[date_index], src)
                row[date_index] = date.strftime(dst)
                writer.writerow(row)


change_date("result.csv", 2, "%Y%m%d", "%Y-%m-%d")
