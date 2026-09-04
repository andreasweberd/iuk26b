def packe_rucksack(fach , snack):
    print(f"🎒 Rucksack wird gepackt...\n"+
    f"-> Buch  für {fach}  eingesteckt.\n"+
    f"-> {snack} als Pausenbrot eingepackt.")
def gehe_weg(strecke_km, geschwindigkeit_kmh):
    dauer = strecke_km / geschwindigkeit_kmh * 60
    print(f"Schulweg wird angetreten...")
    print(f"Für {strecke_km} km brauche ich {dauer} Minuten.")
if __name__ == "__main__":
    packe_rucksack("LF5", "Franzbrötchen")
    gehe_weg(strecke_km=2.5,geschwindigkeit_kmh=50)



