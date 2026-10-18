import sys


def verbrauch_berechnen(kilometer, liter):
    """Berechnet den Durchschnittsverbrauch auf 100 Kilometern."""
    if kilometer <= 0:
        raise ValueError(
            "Die gefahrenen Kilometer müssen größer als 0 sein."
        )
    return (liter / kilometer) * 100


def main():
    print("=== Benzinverbrauch-Rechner ===")

    try:
        # Benutzereingaben abfragen
        km_eingabe = input(
            "Gefahrene Kilometer eingeben (oder 'q' zum Beenden): "
        )
        if km_eingabe.lower() == "q":
            print("Programm beendet.")
            sys.exit()

        liter_eingabe = input("Verbrauchte Liter eingeben: ")

        # Eingaben in Fließkommazahlen (Floats) umwandeln
        kilometer = float(km_eingabe.replace(",", "."))
        liter = float(liter_eingabe.replace(",", "."))

        # Berechnung und Ausgabe
        ergebnis = verbrauch_berechnen(kilometer, liter)
        print(f"\nDein Durchschnittsverbrauch liegt bei: {ergebnis:.2f} l/100km")

    except ValueError as e:
        print(f"\nFehler: Ungültige Eingabe. {e}")
    except ZeroDivisionError:
        print("\nFehler: Kilometer dürfen nicht 0 sein.")


if __name__ == "__main__":
    main()
