numero = int(input("Inserisci un numero: "))
massimo = int(input("Inserisci il massimo: "))
for i in range(massimo, 0, -1):
    if i % numero == 0:
        print(i)