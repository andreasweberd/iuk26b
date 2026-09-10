def packe_rucksack(fach, snack):
    print("🎒 Rucksack wird gepackt...")
    print(f" -> Buch für {fach} eingesteckt.")
    print(f" -> {snack} als Pausenbrot eingepackt.")


def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = (strecke_km / geschwindigkeit_kmh) * 60
    print("🚶 Schulweg wird angetreten...")
    print(f" -> Für {strecke_km} km benötigst du {dauer} Minuten.")


if __name__ == "__main__":
    fach = "LF5"
    snack = "Apfel"
    strecke_km = 2.5
    geschwindigkeit_kmh = 5.0

    packe_rucksack(fach, snack)
    gehe_weg(strecke_km, geschwindigkeit_kmh)
