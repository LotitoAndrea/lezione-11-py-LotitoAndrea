import random

n = int(input("Inserisci un numero: "))
somma = 0
for i in range(1, n+1):
    numero = random.randint(0, 100)
    print(numero)
    somma += numero
print("Somma dei numeri positivi:", somma)