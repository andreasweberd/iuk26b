def Kosten():
    while True:
        try:
            Kilometer = float(input("Wieviele Kilometer sind Sie gefahren? "))
            break
        except ValueError:
            continue
    while True:
        try:
            Liter = float(input("Wieviele Liter haben Sie dabei Verbraucht? "))
            break
        except ValueError:
            continue
    while True:
        try:
            Preis = float(input("Wieviel Kostet 1L Sprit? (in €) "))
            break
        except ValueError:
            continue
    Verbrauch = (Liter * Kilometer) / 100
    print(f"Ihr Verbrauch beträgt {Verbrauch}L/100km")
    Reisekosten = Liter * Preis
    print(f"Die Gesamtkosten für Ihre Reise betragen {Reisekosten}€")
    KilometerPreis = Reisekosten / Kilometer
    print(f"Der Spritpreis pro Kilometer beträgt {KilometerPreis}€")
    if Reisekosten > 50:
        print("Reisekosten sind zu hoch!")
    else:
        print("Reisekosten sind in Ordnung")

if __name__ == "__main__":
    Kosten()