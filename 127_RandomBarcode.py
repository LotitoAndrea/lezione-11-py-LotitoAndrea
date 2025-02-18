import random

for i in range(1,101):
    numero = random.randint(0, 1)
    if numero == 0:
        print(" ", end="")
    else:
        print("|", end="")