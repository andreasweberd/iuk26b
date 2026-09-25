def berechne_reisekosten(distanz, liter, getankte_liter, preis_pro_liter):
    verbrauch = (liter / distanz) * 100
    kosten = getankte_liter * preis_pro_liter
    return verbrauch, kosten


if __name__ == "__main__":
    distanz = float(input("Gebe die Distanz in km ein: "))
    liter = float(input("Gebe die verbrauchten Liter ein: "))
    getankte_liter = float(input("Gebe die getankten Liter ein: "))
    preis_pro_liter = float(input("Gebe den Preis pro Liter ein: "))

    verbrauch, kosten = berechne_reisekosten(distanz, liter, getankte_liter, preis_pro_liter)

    print(f"Der Spritverbrauch beträgt {verbrauch} Liter pro 100 km.")
    print(f"Die Reisekosten betragen {kosten} Euro.")

    if verbrauch >= 8:
        print("Der Spritverbrauch ist hoch.")
    else:
        print("Der Spritverbrauch ist niedrig.")