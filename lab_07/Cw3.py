def sort_mixed_list(args: list, reverse: bool = False) -> list:
    int_list = sorted([x for x in args if isinstance(x, int)])
    str_list = sorted([x for x in args if isinstance(x, str)])
    if reverse:
        return str_list + int_list
    return int_list + str_list


args = [3, 1, 'Ala', 4, 'ma', 0, 'kota', 2]

print(sort_mixed_list(args))
print(sort_mixed_list(args, True))
