from unidecode import unidecode


def group_last_names(last_names):
    a_m = list()
    n_z = list()

    for last_name in last_names:
        nazwisko_uni = unidecode(last_name)

        if 'a' <= nazwisko_uni[0].lower() <= 'm':
            a_m.append(last_name)
        else:
            n_z.append(last_name)

    with open('A-M_nazwiska.txt', 'w') as file:
        for last_name in a_m:
            file.write(last_name + '\n')

    with open('N-Z_nazwiska.txt', 'w') as file:
        for last_name in n_z:
            file.write(last_name + '\n')


group_last_names(['Kowalski', 'Nowak', 'Malinowski', 'Żelichowski'])
