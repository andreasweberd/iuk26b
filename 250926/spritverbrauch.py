def berechne_spritverbrauch(getankte_liter, gefahrene_kilometer):
    return (getankte_liter / gefahrene_kilometer) * 100


if __name__ == '__main__':
    getankte_liter = float(input("getankte Liter eingeben: "))
    gefahrene_kilometer = float(input("gefahrene Kilometer eingeben: "))

    verbrauch = berechne_spritverbrauch(getankte_liter, gefahrene_kilometer)
    print(f"Der Verbrauch ist {verbrauch} l/100 km")

    if (verbrauch > 8):
        print("Du saugst richtig viel du penner")
    else:
        print("normaler Verbrauch o7")
