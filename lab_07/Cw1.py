def extract_numbers(vals: list) -> list:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))


vals = [1, 2.2, '3', 4, 'Ala ma kota']
print(extract_numbers(vals))
