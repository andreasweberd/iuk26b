def tuetwas():
    gefahrene_km = float(input("Wie viele Kilometer bist du gefahren? \n"))
    getankte_liter = float(input("Wie viele Liter Benzin hast du verbraucht? \n"))
    preis_pro_liter = float(input("Wie viel kostet 1 Liter Benzin? \n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100

    gesamtpreis = getankte_liter * preis_pro_liter

    preis_pro_km = gesamtpreis / gefahrene_km

    print(f"\nVerbrauch: {verbrauch:.2f} Liter pro 100 km")
    print(f"Gesamtkosten: {gesamtpreis:.2f} Euro")
    print(f"Kosten pro Kilometer: {preis_pro_km:.2f} Euro")

    if verbrauch > 8:
        print("Verbrauch ist zu hoch")
    else:
        print("Verbrauch ist angemessen")


if __name__ == "__main__":
    tuetwas()