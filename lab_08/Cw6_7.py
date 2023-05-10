from collections import Counter
from collections import deque
import time
import numpy as np
import random


def create_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.elements())


kolo = create_kolo_fortuny('Arek', 'Michał', 'Ala', 'Marek', 'Michał', 'Ania', 'Kacper', 'Szymon')
print(kolo)


def spinit(kolo, ticks: int):
    waits = np.logspace(0.0, 1.0, num=ticks) / ticks

    for tick in range(ticks):
        print(f'{kolo[0]}', end='')
        kolo.rotate()
        time.sleep(waits[tick])
        print('\r', end='')
    print()


spinit(kolo, random.randint(1, 30))
spinit(kolo, random.randint(1, 30))
spinit(kolo, random.randint(1, 30))
spinit(kolo, random.randint(1, 30))
spinit(kolo, random.randint(1, 30))
spinit(kolo, random.randint(1, 30))
