import random


def throw_dice(n: int) -> [(str, str)]:
    throws_count = [0 for _ in range(6)]

    for _ in range(n):
        throws_count[random.randint(0, 5)] += 1

    return [(f'oczka: {i+1}', f'rzutów: {j}') for i, j in enumerate(throws_count) if j != 0]


user_input = int(input('Podaj liczbę rzutów: '))

print(throw_dice(user_input))
