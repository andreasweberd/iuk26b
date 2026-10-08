
if __name__ == "__main__":

    gefahrene_km = float(input("Gefahrene Kilometer angeben als Zahl:\n"))
    getankte_liter = float(input("Getankte Liter angeben als Zahl:\n"))
    spritpreis = float(input("Aktueller Spritpreis pro Liter in €:\n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100
    kosten = getankte_liter * spritpreis
    kosten_pro_km = kosten / gefahrene_km

    print("\nAuswertung")
    print(f"Der Verbrauch lag bei: {verbrauch} Liter pro 100 km")
    print(f"Die Gesamtkosten betragen: {kosten} €")
    print(f"Die Spritkosten pro Kilometer betragen: {kosten_pro_km} €")

    if kosten > 50:
        print("Die Fahrt ist zu teuer!")
    else:
        print("Die Fahrt ist bezahlbar.")
