def kaufen(artikel, preis, anzahl):
    gesamtpreis = (preis * anzahl)
    print("Ich kaufe 3x  für insgesamt", gesamtpreis,  "Euro.")
    
    
    if __name__ == "__main__":
        artikel = "Schokolade"
        preis = 4.5
        anzahl = 3
        kaufen(artikel, preis, anzahl)
     