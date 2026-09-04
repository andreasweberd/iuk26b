def packe_rucksack():
    fach = "Buch für LF5 eingesteckt."
    snack = "Apfel als Pausebrot eingepackt."
    return fach, snack
def gehe_weg():
    strecke_km = 7.5
    geschwindigkeit_kmh = 5.0 
    dauer = (strecke_km / geschwindigkeit_kmh) * 60
    print ("Für", strecke_km, "km benötigst du", dauer, "Minuten.")
if __name__ == "__main__":
    fach, snack = packe_rucksack()
    print (fach)
    print (snack)
    dauer = gehe_weg()
