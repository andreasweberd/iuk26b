def  packe_rucksack(fach, snack):
     print("Rucksack wird gepackt")
     print(f"Buch wird für das {fach} eingepackt")
     print(f"{snack} zum essen")

def gehe_weg(strecke_km, geschwindigkeit_kmh):
     dauer=float (strecke_km / geschwindigkeit_kmh * 60)
     print("gehe Schulweg")
     print(f"für die {strecke_km} km baruchst du {dauer} min")
     



        
if __name__ == "__main__":
    fach = "Lf5"
    snack = "Brötchen"
    strecke = 25 
    geschwindigkeit = 20
    packe_rucksack(fach , snack)
    gehe_weg(strecke , geschwindigkeit)
         


    

