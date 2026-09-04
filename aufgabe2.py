def packe_rucksack(fach, snack):
    print(f'🎒 Rucksack wird gepackt...')
    print(f'-> Buch für {fach} eingesteckt.')
    print(f'-> {snack} als Pausenbrot eingepackt.')


def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = (strecke_km / geschwindigkeit_kmh) * 60
    print(f'🚶 Schulweg wird angetreten...')
    print(f'-> Für {strecke_km} km benötigst du {dauer} Minuten.')


if __name__ == "__main__":
    fach = "LF01"
    snack = "Käsebrot"

    strecke = 2.5
    geschwindigkeit = 4

    packe_rucksack(fach, snack)
    gehe_weg(strecke, geschwindigkeit)
