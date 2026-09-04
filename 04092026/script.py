def packe_rucksack(fach, snack):
    print(f'🎒 Rucksack wird gepackt...\n Buch für {fach} eingesteckt.\n {snack} als Pausebrot eingepackt.')

def gehe_weg(strecke_km, geschwindigkeit_km):
    dauer = (strecke_km / geschwindigkeit_km) * 60
    print(f"🚶 Schulweg wird angetreten...\n Für {strecke_km} km benötigst du {dauer} Minuten.")


if __name__ == '__main__':
    packe_rucksack("LF5", "Brötchen")
    gehe_weg(1.5, 6)