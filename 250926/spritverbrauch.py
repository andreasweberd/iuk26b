def berechne_spritverbrauch(getankte_liter, gefahrene_kilometer):
    return (getankte_liter / gefahrene_kilometer) * 100


def berechne_gesamtkosten(getankte_liter, aktueller_spritpreis):
    return getankte_liter * aktueller_spritpreis


def main():
    getankte_liter = float(input("getankte Liter eingeben: "))
    gefahrene_kilometer = float(input("gefahrene Kilometer eingeben: "))
    aktueller_spritpreis = float(input("GEBE AKTUELLEN SPRITPREIS EIN!!!!!: "))

    verbrauch = berechne_spritverbrauch(getankte_liter, gefahrene_kilometer)
    gesamtkosten = berechne_gesamtkosten(getankte_liter, aktueller_spritpreis)

    print(f"Der Verbrauch ist {verbrauch} l/100 km")
    print(f"Es kostet {gesamtkosten}€")

    if (verbrauch > 8):
        print("Du saugst richtig viel du penner")
    else:
        print("normaler Verbrauch o7")

    if (gesamtkosten > 50):
        print("Zu teuer geh bahn fahren du penner")
    else:
        print("passt vom preis supa")


if __name__ == '__main__':
    main()
