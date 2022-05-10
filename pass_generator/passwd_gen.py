import secrets, random
def generate_pass(length):
    passwd = []
    final_pass = []
    small = list("abcdefghijklmnopqrstuvwxyz")

    capital = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = list("0123456789")
    special = list("@_?$%-+#*!=&")

    #shuffle the lists
    random.shuffle(small)
    random.shuffle(capital)
    random.shuffle(digits)
    random.shuffle(special)

    for i in range(length):
        passwd.append(secrets.choice(small))
        passwd.append(secrets.choice(small))
        passwd.append(random.choice(small))
        passwd.append(secrets.choice(capital))
        passwd.append(secrets.choice(capital))
        passwd.append(secrets.choice(digits))
        passwd.append(secrets.choice(digits))
        passwd.append(secrets.choice(special))
        passwd.append(secrets.choice(special))

    random.shuffle(passwd)

    for i in range(length):
        x = secrets.choice(passwd)
        final_pass.append(x)

    password = "".join(final_pass)#converts list to string
    return password