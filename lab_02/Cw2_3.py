paragraph = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle ' \
            'poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do ' \
            'wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany ' \
            'przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się ' \
            'w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty ' \
            'Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem ' \
            'przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

imie = 'Igor'
nazwisko = 'Boradyn'
litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter1 = paragraph.count(litera_1)
liczba_liter2 = paragraph.count(litera_2)


print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')
