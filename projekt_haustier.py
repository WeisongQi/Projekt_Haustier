# Aufgabe eine Klasse für Haustier


class Haustier:
    def __init__(self, name, species, age, favorite_food, food, energy_level):
        self.nameDesHaustier = name
        self.tierart = species
        self.alterInJahren = age
        self.lieblingsessen = favorite_food
        self.food = food
        self.energy_level = energy_level

    def get_description(self):
        print(
            f"{self.nameDesHaustier} ist ein {self.alterInJahren} alter {self.tierart}, hat {self.energy_level} % Energy."
        )

    def feed(self):
        if self.energy_level < 100:

            f = input(
                f"Bitte wählen Sie das Futter ({self.lieblingsessen} oder {self.food}) für {self.tierart} - {self.nameDesHaustier} : "
            )
            if f == self.lieblingsessen:
                self.energy_level += 30
                print(
                    f"{self.tierart} - {self.nameDesHaustier} liebt {self.lieblingsessen} ! Die Energy ist jetzt {self.energy_level} % ."
                )
            elif f == self.food:
                self.energy_level += 10
                print(
                    f"{self.tierart} - {self.nameDesHaustier} hat {self.food} gegessen. Die Erergie ist jetzt {self.energy_level} % ."
                )
        else:
            print(
                f"{self.tierart} - {self.nameDesHaustier} ist shchon satt, lass uns ein bisschen Bewegung machen. "
            )

    def play(self):
        duration = int(
            input(
                f"Wie lange (in Minuten) willst du mit {self.tierart} - {self.nameDesHaustier} spielen ? "
            )
        )
        verbrauch_energy = duration * 5
        if self.energy_level <= verbrauch_energy:
            self.energy_level = self.energy_level - verbrauch_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} ist müde, muss sich schlafen oder essen."
            )
        else:
            self.energy_level = self.energy_level - verbrauch_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} hat {duration} Minuten gespielt und hat jetzt {self.energy_level} % Energie."
            )

    def sleep(self):
        relex = int(
            input(
                f"Wie lange (in Stunden) willst du  {self.tierart} - {self.nameDesHaustier} schlafen ? "
            )
        )
        new_energy = relex * 20
        if self.energy_level + new_energy >= 100:
            self.energy_level = 100
            print(f"{self.tierart} - {self.nameDesHaustier} ist wieder Da .")
        else:
            self.energy_level = self.energy_level + new_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} muss noch {self.energy_level // 20} Stunden schlafen."
            )


# haustier = Haustier("mimi", "katze", "3 Jahre", "fisch", "cat-manu", 100)
# haustier.get_description()
# haustier.feed()
# haustier.play()
# haustier.sleep()
