import random

eingabe = (input("Geben ein schere/stein/papier: "))
items = ["schere", "stein", "papier"]
auswahl = random.choice(items)
if auswahl == eingabe:
    print(f"{eingabe} | {auswahl} = Unentschieden")
elif eingabe == "schere":
    if auswahl == "stein":
        print(f"{eingabe} | {auswahl} = Du hast verloren")
    else:
        print(f"{eingabe} | {auswahl} = Du hast gewonnen")
elif eingabe == "stein":
    if auswahl == "papier":
        print(f"{eingabe} | {auswahl} = Du hast verloren")
    else:
        print(f"{eingabe} | {auswahl} = Du hast gewonnen")
elif eingabe == "papier":
    if auswahl == "schere":
        print(f"{eingabe} | {auswahl} = Du hast verloren")
    else:
        print(f"{eingabe} | {auswahl} = Du hast gewonnen")

    
