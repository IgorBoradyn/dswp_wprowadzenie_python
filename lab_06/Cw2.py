def merge_files(file_names: list, output_name: str):
    with open(output_name, 'a') as output:
        for file_name in file_names:
            with open(file_name, 'r') as file:
                for line in file:
                    output.write(line)


merge_files(['zamowienia_niemcy.csv', 'zamowienia_polska.csv'], 'zamowienia_polaczone.csv')
