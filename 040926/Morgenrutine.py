def packe_rucksack(fach, snack):
    print(f"\nRucksack wird gepackt...\n-> Buch wird für {fach} eingepackt,\n-> {snack} als Pausenbrot eingepackt")

def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = round(strecke_km / geschwindigkeit_kmh * 60, 2)
    print(f"\nSchulweg wird angetreten...\n-> Für {strecke_km} km benötigst du {dauer} Minuten")

if "__main__" == __name__:
    fach = input("Fach angeben: ")
    snack = input("Snack angeben: ")
    strecke_km = 3.5
    geschwindigkeit_kmh = 4.0


    packe_rucksack(fach, snack)
    gehe_weg(strecke_km, geschwindigkeit_kmh)