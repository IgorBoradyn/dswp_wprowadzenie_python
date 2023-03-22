user_input = input('Wprowadź tekst: ')

unique_chars = list(map(str.lower, set(user_input)))
unique_chars.sort()

print(', '.join(unique_chars))
