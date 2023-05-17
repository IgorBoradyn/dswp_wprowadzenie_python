import os
import csv


def merge_to_csv(folder_path):
    headers = []
    with open('result.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as txt_file:
                            header = next(txt_file).strip()
                            if header not in headers:
                                csv_writer.writerow(header.split(','))
                                headers.append(header)
                            csv_writer.writerows(map(lambda x: x.strip().split(','), txt_file))
                    except StopIteration:
                        pass


merge_to_csv('data_for_lab_10')
