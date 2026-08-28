def main():

    # Berechnet die Kosten eines Einkaufs und gibt den Wert als float zurück.
    def kaufen(artikel, preis, anzahl):
        kosten = float(preis * anzahl)
        print( f"Ich kaufe {anzahl}x {artikel} für {kosten} Euro")
        return kosten

    # Gibt einen String mit einem Antwortsatz mit der Höhe des Rückgeldes zurück, oder eine Verabschiedung
    def rueckGeldGeb(kosten, gegeben):
        rueckGeld = float(kosten - gegeben) 
        if rueckGeld < 0:
            return(f"Du hast zu viel bezahlt. Dein Rückgeld beträgt: {rueckGeld*(-1)} Euro")
        else:
            return (f"Schönen Tag noch")

    # Wrapper Funktion für kaufen und rueckGeldGeb, damit die Funktionsaufrufe gebündelt stattfinden.    
    def einkaufen():
        kosten = kaufen("Schokolade", 1.50, 3)
        answer = rueckGeldGeb(kosten, 10)
        print(answer)


    einkaufen()


if __name__ == "__main__":
    main()


