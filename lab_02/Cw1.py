data = input('Podaj dane: ')
sep_in = input('Podaj separator wejściowy: ')
sep_out = input('Podaj separator wyjściowy: ')

sep_data = data.split(sep_in)
joined_data = sep_out.join(sep_data)

print(joined_data)

# Program służy do zmiany separatora danych w ciągu znaków na inny
# Prostrzym sposobem, aby to osiągnąć jest użycie metody 'replace' na wczytanych danych:
# data_with_replaced_separator = data.replace(sep_in, sep_out)
