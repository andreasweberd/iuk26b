def kaufen(artikel, preis, anzahl):
    kosten = preis * anzahl
    print("Ich kaufe " + str(anzahl) + "x" + str(artikel) + "für insgesamt " + str(kosten) + " Euro.")

if __name__ == '__main__':
    Artikelname = "Schokolade"
    Preis = 1.5
    Anzahl = 3
    kaufen(Artikelname, Preis, Anzahl)