# reisekosten

def main():
    gefahrene_km = float(input("Bitte gefahrenen Kilometer eingeben (zB 15.4)\n"))
    getankte_liter = float(input("Bitte getankte liter eingeben (zB 30.2)\n"))
    spritpreis_pro_liter = float(input("Bitte aktuellen Spritpreis pro Liter in Euro eingebn (zB 2.2)\n"))


    gesamtkosten_fahrt = spritpreis_pro_liter * getankte_liter
    preis_pro_km = gesamtkosten_fahrt / gefahrene_km

    print(f"Der Preis pro km beträgt ca. {preis_pro_km:.2f} €")
    print(f"Die Reisekosten belaufen sich auf {gesamtkosten_fahrt} €")


    if gesamtkosten_fahrt > 50:
        print("Die Kosten sind zu hoch.")
    else:
        print("Die Kosten sind in Ordnung.")

if __name__ == "__main__":
    main()