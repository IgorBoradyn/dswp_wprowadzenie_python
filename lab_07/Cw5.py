from typing import Any


def sort_dict_values(kwargs: dict[Any, list[int]], key):
    for k, v in kwargs.items():
        if not all(isinstance(i, int) for i in v):
            kwargs.pop(k)
    if key is abs:
        return dict(sorted(kwargs.items(), key=lambda x: [key(y) for y in x[1]]))
    return dict(sorted(kwargs.items(), key=lambda x: key(x[1])))


kwargs = {
    'Jan': [1, 3, 4, 7],
    'Maciej': [4, 2, 3, 0],
    'Albert': [10, 5, -30, 15, 11],
}
print(sort_dict_values(kwargs, min))
print(sort_dict_values(kwargs, max))
print(sort_dict_values(kwargs, sum))
print(sort_dict_values(kwargs, abs))
