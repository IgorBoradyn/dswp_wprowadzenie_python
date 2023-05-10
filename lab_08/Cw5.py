def top_10(args):
    size = int(len(args) * 0.1)
    return sorted(args)[-size:]


args = [1, 18, 2, 3, 4, 5, 6, 20, 7, 8, 9, 10, 11, 19, 12, 13, 14, 15, 16, 17]
print(top_10(args))
