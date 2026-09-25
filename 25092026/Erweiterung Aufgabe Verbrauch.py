def verbrauch_berechnen():
    gefahrene_km = float(input("Wie viele Kilometer bist du gefahren? (Komma Zahlen mit Punkt trennen):\n"))
    liter = float(input("Wie viele liter hast du getankt?:\n"))
    tanke = float(input("Wie teuer ist dein sprit?:\n"))
    preis = liter * tanke
    verbrauch = (liter / gefahrene_km) * 100
    preis_pro_km = (verbrauch / 100) + tanke
    print(f"Du hattest einen verbrauch von {round(verbrauch),2}l/100KM")
    if verbrauch > 8:
        print("Dein Verbrauch ist hoch")
    else:
        print("Dein Verbrauch ist nicht hoch")
    print(f"Du hast für {preis}€ getankt")
    print(f"Du hast {round(preis_pro_km),2}€ für jeden gefahrenen Kilometer bezahlt")

    if preis > 50.0:
        print("Der Trip ist zu teuer!!")
    else:
        print("Der Trip ist bezahlbar.")

if __name__ == '__main__':
    verbrauch_berechnen()