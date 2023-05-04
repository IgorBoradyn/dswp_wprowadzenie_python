def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


print(reverse_words('Ala ma kota'))
