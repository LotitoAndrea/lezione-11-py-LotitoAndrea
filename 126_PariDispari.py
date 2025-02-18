contatore = 0
for i in range(1,12):
    if i % 2 == 0:
        print("*")
    else:
        contatore += 1
        print("*" * contatore)