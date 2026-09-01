def Einkauf():

    def kaufen(artikel, preis, anzahl):
        global gesammt        
        gesammt = (preis * anzahl)
        print(f"Ich habe {anzahl}mal {artikel} gekauft für insgesammt {gesammt}€")


    def bezahlen(einzahlung, gesammt):
        rueckzahlung = (einzahlung - gesammt)
        if rueckzahlung > 0:
            print(f"Mein Rückgeld beträgt {rueckzahlung}€.")
        else:
            print(f"Ich wünsche Ihnen einen schönen Tag!")

    kaufen("Schokolade", 5, 3)
    bezahlen(20, gesammt)

if __name__ == "__main__":
    Einkauf()