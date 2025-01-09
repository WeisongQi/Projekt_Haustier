# Spiel
from projekt_haustier import Haustier


haustiere = []

while True:
    print("\nMenü:")
    print("1. Erstelle ein neues Haustier")
    print("2. Zeige alle Haustiere")
    print("3. Füttere ein Haustier")
    print("4. Spiele mit einem Haustier")
    print("5. Lass ein Haustier schlafen")
    print("6. Beende das Programm")

    wahl = input("Wähle eine Option: ")

    if wahl == "1":
        name = input("Name des Haustiers: ")
        species = input("Tierart: ")
        age = input("Alter: ")
        favorite_food = input("Lieblingsessen: ")
        food = input("Food: ")
        energy_level = int(input("Energielevel: "))
        haustier = Haustier(name, species, age, favorite_food, food, energy_level)
        haustiere.append(haustier)
        print(f"{name} wurde erstellt.")
    elif wahl == "2":
        for i, haustier in enumerate(haustiere):
            print(f"\nHaustier {i + 1}:")
            haustier.get_description()
    elif wahl == "3":
        index = (
            int(input("Welches Haustier möchtest du füttern (Nummer eingeben): ")) - 1
        )
        if 0 <= index < len(haustiere):
            haustiere[index].feed()
        else:
            print("Ungültige Nummer.")
    elif wahl == "4":
        index = (
            int(input("Mit welchem Haustier möchtest du spielen (Nummer eingeben): "))
            - 1
        )
        if 0 <= index < len(haustiere):
            haustiere[index].play()
        else:
            print("Ungültige Nummer.")
    elif wahl == "5":
        index = int(input("Welches Haustier soll schlafen (Nummer eingeben): ")) - 1
        if 0 <= index < len(haustiere):
            haustiere[index].sleep()
        else:
            print("Ungültige Nummer.")
    elif wahl == "6":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Wahl. Bitte versuche es erneut.")
