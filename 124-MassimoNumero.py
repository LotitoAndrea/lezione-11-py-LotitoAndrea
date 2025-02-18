massimo = int(input("Inserisci un numero: "))
for i in range (1, massimo + 1):
    numero = int(input("Inserisci il numero " + str(i) + ": "))
massimo = max(massimo, numero)
print("Il massimo numero inserito è: ", massimo)