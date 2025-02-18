numero = int(input("Inserisci un numero: "))
if numero == 0:
    print("Il numero", numero, "non è primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("Il numero", numero, "non è primo.")
            break
    else:
        print("Il numero", numero, "è primo.")