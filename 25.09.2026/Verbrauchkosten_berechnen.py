from Spritverbrauch_berechnen import berechne_verbrauch

def kosten_berechnen(liter, kosten_pro_liter):
    return round(liter * kosten, 2)

def kosten_berechnen_pro_km(gefahrene_km, liter, kosten_pro_liter):
    verbrauch_pro_km = berechne_verbrauch(gefahrene_km, liter) / 100
    return round(kosten_berechnen(verbrauch_pro_km, kosten_pro_liter), 2)

if __name__ == "__main__":
    gefahrene_km = float(input("Gib die gefahrenen km an (z.B.: 148.4): "))
    liter = float(input("Gib die verbrauchten Liter an (z.B.: 10.6): "))
    kosten = float(input("Gib den aktuellen Preis in Euro pro Literan (z.B.: 1.7): "))

    gesamt_preis = kosten_berechnen(liter, kosten)
    preis_pro_km = kosten_berechnen_pro_km(gefahrene_km, liter, kosten)

    print(f"Die Gesamtkosten liegen bei {gesamt_preis}Euro,\ndie Kosten pro km liegen bei {preis_pro_km}Euro.")
    if gesamt_preis > 100:
        print("Die Fahrt ist zu teuer.")
    else:
        print("Die Fahrt ist nicht zu teuer.")
