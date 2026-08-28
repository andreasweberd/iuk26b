def main():

    def kaufen(artikel, preis, anzahl):
        kosten = float(preis * anzahl)
        return f"ich kaufe {anzahl}x {artikel} für {kosten} Euro"

    print (kaufen("Schokolade", 1.5, 3))



if __name__ == "main":
    main()