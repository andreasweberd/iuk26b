def main():

    def packe_rucksack(fach: str, snack: str):
        print(f"🎒 Rucksack wird gepackt... \n -> Buch für {fach} eingesteckt \n -> {snack} als Pausenbrot eingepackt")
    

    def gehe_weg(strecke_km: float, geschwindigkeit_kmh: float):
        print(f"🚶 Schulweg wird angetreten... \n -> für {strecke_km} km benötigst du {strecke_km / geschwindigkeit_kmh * 60} Minuten")

    packe_rucksack("Mathematik", "Apfel")
    gehe_weg(2.5, 5.0)

if __name__ == "__main__":
    main()