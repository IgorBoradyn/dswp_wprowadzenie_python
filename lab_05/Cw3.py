user_input = input('Podaj zdanie: ')
words = user_input.split(' ')

result = [(x, [ord(y) for y in x]) for x in words]

print(result)
