import string

user_input = input("Wprowadź tekst: ")

text = user_input.lower()

ascii_lowercase_count = sum(1 for i in text if i in string.ascii_lowercase)
digits_count = sum(1 for i in text if i in string.digits)

ascii_lowercase_percentage = (ascii_lowercase_count/len(text)) * 100
digits_percentage = (digits_count/len(text)) * 100

print(f'ascii_lowercase_count: {ascii_lowercase_count}, ascii_lowercase_percentage: {ascii_lowercase_percentage}')
print(f'digits_count: {digits_count}, digits_percentage: {digits_percentage}')
