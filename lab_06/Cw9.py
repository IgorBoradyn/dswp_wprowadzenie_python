import random

with open('hasla.txt', 'r') as f:
    phrases = [line.strip() for line in f]

phrase = random.choice(phrases).lower()

visible = set(' ')
hidden = set(phrase)
hidden.remove(' ')

while len(hidden) != 0:

    for char in phrase:
        if char in visible:
            print(char, end='')
        else:
            print('_', end='')
    print()

    char = input('Podaj literę lub wpisz hasło: ').lower()

    if char == phrase:
        break

    if char in hidden:
        visible.add(char)
        hidden.remove(char)
    else:
        print('Podana litera nie występuje w haśle!')

print('Gratulacje, odgadłeś hasło!')
