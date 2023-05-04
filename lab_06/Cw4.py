def group_by_type(values):
    result = {}
    for element in values:
        t = type(element).__name__
        if t not in result:
            result[t] = []
        result[t].append(element)
    return result


print(group_by_type([1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]))
