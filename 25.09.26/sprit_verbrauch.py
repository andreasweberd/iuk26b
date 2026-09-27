# spritverbrauch

def main():
    gefahrene_km = float(input("Bitte gefahrenen Kilometer eingeben (zB 15.4)\n"))
    getankte_liter = float(input("Bitte getankte liter eingeben (zB 30.2)\n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100

    print(f"Der Verbrauch lag bei ca. {verbrauch:.2f} l/100 km")

    if verbrauch > 8:
        print("Der Verbrauch ist zu hoch.")
    else:
        print("Das Fahrzeug ist sparsam.")

if __name__ == "__main__":
    main()