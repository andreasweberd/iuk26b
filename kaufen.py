def kaufen(artikel, preis, anzahl):
    return f"Ich kaufe {anzahl} {artikel} für insgesamt {preis * anzahl} Euro."


if __name__ == "__main__":
    artikel = "Käsebrot"
    preis = 2.5
    anzahl = 3

    ausgabe = kaufen(artikel, preis, anzahl)
    print(ausgabe)
