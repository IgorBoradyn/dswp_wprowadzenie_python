import re

with open('strings.txt', 'r') as file:
    content = file.read()

numbers = re.findall(r'\d+', content)
numbers_3_digits = re.findall(r'\d{3,}', content)
ips = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', content)
capitalized_start = re.findall(r'[A-Z]\w*', content)
at_least_4_words = re.findall(r'\w+ \w+ \w+ [\S ]+', content)
urls = re.findall(r'https://\S+', content)

print(numbers)
print(numbers_3_digits)
print(ips)
print(capitalized_start)
print(at_least_4_words)
print(urls)
