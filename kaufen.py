def kaufen(artikel, preis, anzahl):
    kosten = preis * anzahl
    print("Ich kaufe " + str(anzahl) + "x " + str(artikel) + " für insgesamt " + str(kosten) + " Euro.")

if __name__ == '__main__':
    artikelname = "Schokolade"
    preis = 1.5
    anzahl = 3
    kaufen(artikelname, preis, anzahl)