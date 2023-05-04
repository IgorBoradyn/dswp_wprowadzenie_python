def n_values(n, values, largest=True):
    if all(isinstance(x, (int, float)) for x in values):
        if largest:
            return sorted(values)[-n:]
        else:
            return sorted(values)[:n]
    else:
        return "Lista zawiera elementy niebędące liczbami"


print(n_values(2, [1, 2, 3, 4, 5, 6, 7, 8], True))
print(n_values(4, [1, 2, 3, 4, 5, 6, 7, 8], False))
