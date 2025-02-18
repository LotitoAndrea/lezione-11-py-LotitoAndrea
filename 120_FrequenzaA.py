parola = input("Inserisci una parola: ")
contatore = 0
for i in parola:
    if i == "a":
        contatore += 1
print("sono state trovare", contatore, "a")