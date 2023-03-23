def sum_scores(**kwargs: {str: int}):
    return sum(kwargs.values())


scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
}

print(sum_scores(**scores))
