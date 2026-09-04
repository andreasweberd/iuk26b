

def packe_rucksack(fach , snack):
    print("🎒 Rucksack wird gepackt...")
    print(f" -> Buch für {fach} eingesteckt.")
    print(f" -> {snack} als Pausenbrot eingepackt.")


def gehe_weg(strecke_km , geschwindigkeit_kmh):
    dauer=round(strecke_km / geschwindigkeit_kmh * 60, 2)
    print("trete Schulweg an...")
    print(f"Für {strecke_km} km benötigst du {dauer} min")

if __name__ == "__main__":
    fach = "L5"
    snack = "Käsebrot"
    strecke = 13.5
    speed = 7
    packe_rucksack(fach , snack)
    gehe_weg(strecke , speed)