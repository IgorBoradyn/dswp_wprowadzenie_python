words = input("Podaj wyrazy oddzielone spacją: ").split()

sorted_words = sorted(words, key=lambda x: len(x), reverse=True)

print(sorted_words)
