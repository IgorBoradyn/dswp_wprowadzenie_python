import this

while True:
    user_input = input("Wpisz zdanie: ")
    encoded_text = ""

    for letter in user_input:
        try:
            encoded_text += this.d[letter]
        except KeyError:
            encoded_text += letter

    print("Zakodowane zdanie: ", encoded_text)
