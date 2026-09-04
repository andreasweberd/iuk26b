def main():

    def kaufen(artikel, preis, anzahl):
        kosten = float(preis * anzahl)
        return f"ich kaufe {anzahl}x {artikel} für {kosten} Euro"

    print (kaufen("Schokolade", 1.5, 3))

def rueckgeldGeben(kosten, gegeben):
    rueckgeld=float (gegeben - kosten)
    print (f"Hier dein Geld {rueckgeld}")


if __name__ == "__main__":
    main()