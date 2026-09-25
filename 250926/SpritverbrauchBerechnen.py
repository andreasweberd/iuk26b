if __name__=="__main__":
    # eingabe der KM Anzahl, float macht dass nur zahlen (auch kommazahlen eingefügt werden) /n macht das beim input eine neue zeile als eingabeort gezeigt wird
    gefahrene_km = float(input("Wie viele kilometer gefahren als Zahl?\n"))
    getankte_liter = float(input("Wie viele Liter Sprit getankt als Zahl?\n"))
    spritpreis = float(input("Wie viel kostet 1 Liter Sprit in Euro? \n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100
    gesamtkosten = getankte_liter * spritpreis

    print(f"Der Verbrauch lag bei {verbrauch}L pro 100km")
    print(f"Die Gesamtkosten für die Fahrt beträgt {gesamtkosten} Euro")

    if gesamtkosten > 50.0:
        print("Die Fahrt ist zu teuer!")
    else:print("Die Kosten sind in Ordnung, Gute Fahrt!")

    if verbrauch >8:
        print("Der Verbrauch ist hoch!")
    else:
        print("Der Verbrauch ist sparsam!")