import sys

print('Podaj liczbę: ')
user_input = sys.stdin.readline()
value = int(user_input)

output = []
magnitude = 1

while value >= magnitude:
    digit = int(value / magnitude) % 10

    output.append(f'{str(magnitude)} * {str(digit)}')
    output.append('+')

    magnitude *= 10

output[-1] = 'Podaną liczbę można zapisać jako:'

sys.stdout.write(' '.join(output[::-1]))
