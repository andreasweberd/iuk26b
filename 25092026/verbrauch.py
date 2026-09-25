def verbrauch_berechnen():
    gefahrene_km = float(input("Wie viele Kilometer bist du gefahren? (Komma Zahlen mit Punkt trennen):\n"))
    liter = float(input("Wie viele liter hast du verbraucht?:\n"))
    verbrauch = (liter / gefahrene_km) * 100
    print(f"Du hattest einen verbrauch von {verbrauch} l/100KM")
    if verbrauch > 8:
        print("Dein Verbrauch ist hoch")
    else:
        print("Dein Verbrauch ist nicht hoch")

if __name__ == '__main__':
    verbrauch_berechnen()