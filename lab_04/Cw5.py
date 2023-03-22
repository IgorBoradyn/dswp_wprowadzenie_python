user_input = input('Wpisz zdanie: ')

words = user_input.split(' ')

words.sort(key=len)

print(words)
