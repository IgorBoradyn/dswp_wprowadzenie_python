from unidecode import unidecode


def generate_emails(file_name, domain):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        with open('emaile.txt', 'w') as output:
            for line in lines:
                name = line.strip().split()
                name = [unidecode(x) for x in name]
                email = f"{name[0]}.{name[1]}@{domain}"
                output.write(f"{line.strip()}, {email}\n")


generate_emails('osoby.txt', 'wp.pl')
