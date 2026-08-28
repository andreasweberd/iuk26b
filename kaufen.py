def preis_identifizieren(artikel):
    preise = {
        "Käsebrot": 2.5,
        "Wurstbrot": 3.0,
        "Salat": 4.0,
        "Getränk": 1.5
    }
    return preise.get(artikel, "Artikel nicht gefunden")


def kaufen(artikel, preis, anzahl):
    kosten = preis * anzahl
    print(f"Ich kaufe {anzahl} {artikel} für insgesamt {kosten} Euro.")
    return kosten


def rueckgeldGeben(preis, gegeben):
    rueckgeld = gegeben - preis
    if rueckgeld < 0:
        print(
            f"Du hast nicht genug Geld gegeben. Du brauchst noch {abs(rueckgeld)} €.")
    else:
        print(f"Hier ist dein Rückgeld: {rueckgeld} €.")


if __name__ == "__main__":
    artikel = "Käsebrot"
    anzahl = 3
    gegeben = 3

    preis = preis_identifizieren(artikel)
    kosten = kaufen(artikel, preis, anzahl)
    rueckgeldGeben(kosten, gegeben)
