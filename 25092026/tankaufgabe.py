def main():

    # Funktion, um die Werte von dem User zu erhalten und zu überprüfen.
    def get_values():
        km = input("Gebe die gefahrenen Kilometer an: ")
        l = input("Gebe die getankten Liter an: ")

        # Wenn einer der Werte nicht zu einem float konvertiert werden kann, dann wird die Funktion mit einer Meldung erneut ausgeführt.
        try:
            float(km)
            float(l)
        except:
            print("Bitte gebe die Werte als Gleitkommazahl mit einem Punkt separiert und ohne Einheit an!")
            get_values()

        return {'km': km, 'l': l}

    # Funktion um den Verbrauch/100km zu errechnen.
    # Der Verbrauch wird zusammen mit einer verbrauchsbezogenen Angabe ausgegeben.
    def calc_fuel_consumption(val):
        fuel_consumption = float(val['l'])/float(val['km'])*100
        print(f"Der Verbrauch lag bei {fuel_consumption}l/100km")

        if fuel_consumption > 8:
            print("Hoher Verbrauch!")
        else:
            print("Sparsam!")

    # Verschachtelter Funktionsaufruf um den Verbrauch zu errechnen und eine direkte Ausgabe zu tätigen.
    calc_fuel_consumption(get_values())

if __name__ == "__main__":
    main()