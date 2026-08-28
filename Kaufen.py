def kaufen(artikel, preis, anzahl):
    gesammt = preis * anzahl 
    print(f"Ich habe {anzahl}x {artikel} gekauft für {gesammt}€")

if __name__ == "__main__":
    kaufen("Schokolade", 5, 3)