def kaufen(artikel, preis, anzahl):
    kosten = preis*anzahl
    print(f"Ich kaufe {anzahl} x {artikel} für insegsamt {kosten}")

if __name__ == "__main__":
    kaufen("Brot", 2.35, 2)
