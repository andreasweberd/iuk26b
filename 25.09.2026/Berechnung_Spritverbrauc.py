def berechne_spritverbrauch(distanz, liter):
    verbrauch = (liter / distanz) * 100
    return verbrauch
    

if __name__ == "__main__":
    distanz = float(input("Gebe die distanz in km ein:"))
    liter = float(input("Gebe die verbrauchten liter ein:"))
    verbrauch = berechne_spritverbrauch(distanz, liter)
    print(f"Der Spritverbrauch beträgt {verbrauch} Liter pro 100 km.")

    if verbrauch >= 8:
        print("Der Spritverbrauch ist hoch.")
    else:
        print("Der Spritverbrauch ist niedrig.")