    # 🎒 Rucksack wird gepackt...
    #  -> Buch für LF5 eingesteckt.
    #  -> Apfel als Pausebrot eingepackt.
    # 🚶 Schulweg wird angetreten...
    #  -> Für 2.5 km benötigst du 30.0 Minuten.

def packe_rucksack(fach, snack):
    print("🎒 Rucksack wird gepackt...")
    print(f"-> Buch für {fach} eingesteckt.")
    print(f"-> {snack} als Pausebrot eingepackt.")

def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = round((float(strecke_km) / float(geschwindigkeit_kmh) * 60), 2)
    print("🚶 Schulweg wird angetreten...")
    print(f"-> Für {strecke_km}km benötigst du  {dauer} Minuten.")

if __name__ == "__main__":
    packe_rucksack("Freistunde", "Energy")
    gehe_weg("42.2", "20")