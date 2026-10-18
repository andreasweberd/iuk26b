# das ist ein KaufPlatform

def kaufen(artikel, preis, anzahl):
    gesamt = preis * anzahl

    print(f"Ich kaufe {anzahl}x {artikel} für insgesamt {gesamt} Euro.")


if __name__ == "__main__":

    artikel_name = "Pizza"
    artikel_preis = 10
    artikel_anzahl = 1

    kaufen(artikel_name, artikel_preis, artikel_anzahl)