#
def packe_rucksack(fach , snacks):
    print("Buch für " + fach + " gepackt!")
    print(f"{snacks} als Pausenbrot eingepackt!")

def gehe_weg(strecke_km , geschwindigkeit_kmh):
    dauer = strecke_km / geschwindigkeit_kmh * 60
    print(f"Für {strecke_km:.2f} km brauche ich {dauer:.2f} Minuten.")

if __name__ == "__main__":
    input_fach = input("Welches Fach ?: ")
    input_snacks = input("Welcher Snack ?: ")
    packe_rucksack(input_fach , input_snacks)

    input_strecke = float(input("Wie viele km sind es ?: "))
    input_geschwindigkeit = float(input("Geschwindigkeit (in km/h)?: "))
    gehe_weg(input_strecke , input_geschwindigkeit)

    