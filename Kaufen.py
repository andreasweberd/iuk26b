def kaufen(artikel, preis, anzahl):
    gesammt = preis * anzahl 
    print(f"Gesammtpreis des Einkaufs {gesammt}€")
    print("Ich habe 3x Schokolade gekauft für 4,50€")

if __name__ == "__main__":
    kaufen(1, 3, 5)