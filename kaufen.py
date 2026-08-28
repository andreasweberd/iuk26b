# Uebungsaufgabe 28.8.26 Weber LF5
#
def kaufen (artikel, preis, anzahl):
    gesamt = preis + anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamt} Euro. ")

if __name__ == "__main__":
    artikel = "Schokolade"
    preis = 1.5
    anzahl = 3

    kaufen(artikel, preis, anzahl)