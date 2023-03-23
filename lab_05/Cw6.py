def sort_str(*args) -> [str]:
    result = list(*args)
    result.sort()

    return result


words = ('kota', 'Ala', 'ma')

print(sort_str(words))
