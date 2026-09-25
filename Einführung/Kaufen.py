def kaufen (artikel, preis, anzahl):
    gesamtpreis = preis * anzahl
    print ("Ich kaufe 3x Schokolade für insgesamt", gesamtpreis, "Euro.")
    return gesamtpreis

def rueckgeld (rueckgeldGeben):
    print ("Ich habe 10 Euro gegeben, also bekomme ich", rueckgeldGeben, "Euro zurück.")    

if __name__ == "__main__":
    artikel = "Schokolade"
    preis = 2.50
    anzahl = 3

    gesamtpreis = kaufen(artikel, preis, anzahl)
    rueckgeldGeben = 10 - gesamtpreis
    rueckgeld(rueckgeldGeben)
    