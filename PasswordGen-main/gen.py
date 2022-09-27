import random as rand

char = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStRuUvVwWxXyYzZ1234567890"

limit = int(input("Please set a limit for your password\nEnter here: "))

if limit > 20:
    print("That is too big!")
else:
    p = rand.choices(char, k=limit)
    password = "".join(p) + "!"
    print(password)

file = open("passwords.txt", "a")
file.write(password + "\n")
file.close()