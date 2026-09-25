def main():

    # Funktion, um die Werte von dem User zu erhalten und zu überprüfen.
    def get_values():
        km = input("Gebe die gefahrenen Kilometer an: ")
        l = input("Gebe die getankten Liter an: ")
        p = input("Was kostet ein Liter Diesel oder Benzin aktuell pro Liter? ")

        # Wenn einer der Werte nicht zu einem float konvertiert werden kann, dann wird die Funktion mit einer Meldung erneut ausgeführt.
        try:
            float(km)
            float(l)
            float(p)
        except:
            print("Bitte gebe die Werte einem Punkt separiert und ohne Einheit an!")
            get_values()

        return {'km': km, 'l': l, 'p': p}

    def calc_output_val(val):
        fuel_consumption = float(val['l'])/float(val['km'])*100

        trip_cost = float(val['l'])*float(val['p'])

        cost_per_km = fuel_consumption/100*float(val['p'])

        print(f"Der Verbrauch lag bei {round(fuel_consumption, 2)}l/100km \nDiese Fahrt hat {round(trip_cost, 2)}€ gekostet \nDie kosten pro Kilometer liegen bei {round(cost_per_km, 2)}€")

        if (trip_cost > 50):
            print("Die Kosten sind zu hoch!")
        else:
            print("Die Kosten sind in Ordnung.")

    calc_output_val(get_values())


if __name__ == "__main__":
    main()