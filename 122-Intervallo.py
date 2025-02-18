numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))
if numero2 < numero1:
    print("Il secondo numero deve essere maggiore del primo.")
else:
    somma = 0
    for i in range(numero1, numero2+1):
        somma += i
    print("Somma dei numeri nell'intervallo:", somma)