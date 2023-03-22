user_input = input('Podaj wartość: ')

try:
    if str(int(user_input)) == user_input:
        print('Wartość pozostaje niezmieniona po rzutowaniu na int')
    else:
        print('Wartość zostaje zmieniona po rzutowaniu na int')

    print('Wartość jest rzutowalna na int')
except ValueError:
    print('Wartość nie jest rzutowalna na int')

try:
    if str(float(user_input)) == user_input:
        print('Wartość pozostaje niezmieniona po rzutowaniu na float')
    else:
        print('Wartość zostaje zmieniona po rzutowaniu na float')

    print('Wartość jest rzutowalna na float')
except ValueError:
    print('Wartość nie jest rzutowalna na float')
