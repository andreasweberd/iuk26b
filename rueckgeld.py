# Uebungsaufgabe 28.8.26 Weber LF5
#
def kaufen (artikel, preis, anzahl):
    gesamt = preis + anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamt} Euro. ")
    return gesamt

def rueckgeldgeben(preis, gegeben):
    rueckgeld = gegeben - preis
    print(f"Hier dein Rückgeld: {rueckgeld} Euro.")

if __name__ == "__main__":
    artikel = "Schokolade"
    preis = 1.5
    anzahl = 3
    geldgegeben = 10

    kaufen(artikel, preis, anzahl)
    rueckgeldgeben(preis, geldgegeben)