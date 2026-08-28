def main():

    def kaufen(artikel, preis, anzahl):
        kosten = float(preis * anzahl)
        return f"Ich kaufe {anzahl}x {artikel} für {kosten} Euro"


    print(kaufen("Schokolade", 1.50, 3))


if __name__ == "__main__":
    main()


