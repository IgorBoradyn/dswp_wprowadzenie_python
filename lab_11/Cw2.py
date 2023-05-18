import csv
from datetime import datetime
import re

with open('logs.txt', 'r') as txt_file:
    with open('logs.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

        writer.writerow(['date', 'ip', 'user', 'message'])

        for i, line in enumerate(txt_file):
            d = re.findall(r'^\w+ +\d+ \d+:\d+:\d+', line)[0]
            line = line[len(d)+1:]
            ip = re.findall(r'^ip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}', line)[0]
            line = line[len(ip)+1:]
            user = re.findall(r'^[^:]+', line)[0]
            line = line[len(user)+1:].strip()

            d = datetime.strptime(d, '%b %d %H:%M:%S').replace(year=datetime.now().year)
            d = d.strftime("%Y-%m-%d %H:%M:%S")
            ip = ip.replace('-', '.')[3:]
            user = re.findall(r'^[^\[]+', user)[0]

            writer.writerow([d, ip, user, line])
