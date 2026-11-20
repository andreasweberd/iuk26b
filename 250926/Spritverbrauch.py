def verbrauch_berechnen(kilometer, liter):
    verbrauch = (liter / kilometer) * 100
    gesamtkosten = round (liter * preis_pro_liter, 2)
    print(f"Verbrauch: {verbrauch} Liter pro 100 km")
    print(f"Gesamtkosten der Fahrt: {gesamtkosten} Euro")
    if verbrauch > 8:
        print("Hoher Verbrauch!")
    else:
        print("Sparsam!")

if __name__ == "__main__":
    kilometer = float(input("Gefahrene Kilometer: ")) #float erzwingt eine , zahl
    liter = float(input("Getankte Liter: "))
    preis_pro_liter = float(input("Preis pro Liter: "))
    verbrauch_berechnen(kilometer, liter)