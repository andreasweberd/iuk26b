def verbrauch_berechnen(kilometer, liter):
    verbrauch = (liter / kilometer) * 100
    print(f"Verbrauch: {verbrauch} Liter pro 100 km")
    if verbrauch > 8:
        print("Hoher Verbrauch!")
    else:
        print("Sparsam!")

if __name__ == "__main__":
    verbrauch_berechnen(500, 45)