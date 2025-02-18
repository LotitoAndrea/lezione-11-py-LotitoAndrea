import random

n = int(input("Inserisci un numero: "))
sommaPositivi = 0
sommaNegativi = 0
for i in range(1, n+1):
    numero = int(input("Inserisci il numero ", str(i), ": "))
    if numero > 0:
        sommaPositivi += numero
    else:
        sommaNegativi += numero
print("Somma dei numeri positivi:", sommaPositivi)
print("Somma dei numeri negativi:", sommaNegativi)