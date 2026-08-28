def kaufen(artikel, preis,anzahl):
    kosten = preis * anzahl
    print(f"Ich kaufe {anzahl} {artikel} für insgesamt {kosten} Euro")

if __name__ == '__main__':
    kaufen("RedBull", 2.95, 5)
    kaufen("schokocroissant", 2.75, 2)
    kaufen("schokolade", 0.99, 7)

