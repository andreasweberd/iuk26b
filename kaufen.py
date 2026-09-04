def kaufen(artikel, preis, anzahl):
    kosten = preis * anzahl
    return kosten

    def rueckgeldGeben(preis, gegeben):
        rueckgeld = gegeben - preis
        return rueckgeld

if __name__ == '__main__':

    # variablem zum Kauf
    artikelname = "Schokolade"
    preis = 1.5
    anzahl = 3
    gegeben = 10

    # Ausfuehren der Methoden und Feedback via print
    kosten = kaufen(artikelname, preis, anzahl)
    rueckgeld = rueckgeldGeben(kosten, gegeben)
    print(f"Ich kaufe {anzahl}x {artikelname} für insgesamt {kosten} Euro.\nEs wurden {gegeben} Euro bezahlt.\nDas ruekgeld betraegt: {rueckgeld}.")