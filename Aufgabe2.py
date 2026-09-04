
def     packe_rucksack(fach,snack):

    print(f"stecke buch für {fach} ein")
    print(f"{snack} als pausenbrot")

def     gehe_weg(strecke_km,geschwindigkeit_kmh):
    dauer = (strecke_km / geschwindigkeit_kmh) *60
    print(f"für {strecke_km} brauche ich {dauer}")

if __name__ == "__main__":

    strecke_km = 1.5
    geschwindigkeit_kmh = 9.5
    gehe_weg (strecke_km,geschwindigkeit_kmh)

    fach = "LF5"
    snack= "käsebrot"
    packe_rucksack (fach,snack)
