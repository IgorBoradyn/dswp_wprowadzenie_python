import random

sentences = [
    [
        'Koleżanki i koledzy',
        'Z drugiej strony',
        'Podobnie',
        'Nie zapominajmy jednak, że',
        'W ten oto sposób',
        'Praktyka dnia codziennego dowodzi, że',
        'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
        'Różnorakie i bogate doświadczenia',
        'Troska organizacji, a szczególnie',
        'Wyższe założenia ideowe, a także',
    ],
    [
        'realizacja nakreślonych zadań programowych',
        'zakres i miejsce szkolenia kadr',
        'stały wzrost ilości i zakres naszej aktywności',
        'aktualna struktura organizacji',
        'nowy model działalności organizacyjnej',
        'dalszy rozwój różnych form działalności',
        'stałe zabezpieczenie informacyjno programowe naszej działalności',
        'wzmacnianie i rozwijanie struktur',
        'konsultacja z szerokim aktywem',
        'rozpoczęcie powszechnej akcji kształtowania postaw',
    ],
    [
        'zmusza nas do przeanalizowania',
        'spełnia istotną rolę w kształtowaniu',
        'wymaga sprecyzowania i określenia',
        'pomaga w przygotowaniu i realizacji',
        'zabezpiecza udział szerokiej grupie w kształtowaniu',
        'spełnia ważne zadania w wypracowaniu',
        'umożliwia w większym stopniu tworzenie',
        'powoduje docenianie wagi',
        'przedstawia intersującą próbę sprawdzenia',
        'pociąga za sobą proces wdrażania i unowocześniania',
    ],
    [
        'istniejących warunków administracyjno-finansowych.',
        'dalszych kierunków rozwoju.',
        'systemu powszechnego uczestnictwa.',
        'postaw uczestników wobec zadań stawianych przez organizację.',
        'nowych propozycji.',
        'kierunków postępowego wychowania.',
        'systemu szkolenia kadry odpowiadającego potrzebom.',
        'odpowiednich waruknków aktywizacji.',
        'modelu rozwoju.',
        'form oddziaływania.',
    ],
]

user_input = int(input('Podaj liczbę zdań: '))

for i in range(user_input):
    sentence = []

    for j in range(4):
        sentence.append(
            sentences[j][random.randint(0, 9)]
        )

    print(' '.join(sentence))

