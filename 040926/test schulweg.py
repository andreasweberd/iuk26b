def packe_rucksack(fach, snack):
    print("    🎒 Rucksack wird gepackt...\n"+
     f"-> Buch für {fach} eingesteckt.\n"+
     f"-> {snack} als Pausenbrot eingepackt.")

def gehe_weg(strecke_km, geschwindigkeit_kmh):
    print("    🚶 Schulweg wird angetreten...\n"+
     "-> Für {strecke_km} km benötigst du {dauer_min} Minuten.")

if __name__ == "__main__":
    packe_rucksack("LF5", "Nutella")
    gehe_weg("2.5", "Nutella")