def packe_rucksack(fach, snack):
    print("\n", "Rucksack wird gepackt...","\n", "Buch für", fach, "eingesteckt.", "\n", snack, "als Pausebrot eingepackt.")
    # print(f"Rucksack wird gepackt...\n"+
    #       f"-> Buch für {fach} eingesteckt.\n"+
    #       f"-> {snack} als Pausebrot eingepackt.")

def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = (strecke_km / geschwindigkeit_kmh) * 60
    print("\n", "Schulweg wird angetreten...", "\n", "Für ", strecke_km, "benötigst du ", dauer, " Minuten.")

if __name__ == '__main__':
    packe_rucksack('LF5', 'Apfel')
    gehe_weg(2.5, 5)