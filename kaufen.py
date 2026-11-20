
def einkaufen(artikel, anzahl, preis):
    gesamt = preis * anzahl
    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamt}€.")

if __name__ == "__main__":
    artikel = "Schokolade"
    preis = 1.5
    anzahl = 3

    # KORREKTUR: anzahl und preis in der richtigen Reihenfolge übergeben
    einkaufen(artikel, anzahl, preis)

