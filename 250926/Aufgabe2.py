if __name__ == "__main__":
    
    gefahrene_km = float(input("Gefahrene Kilometer:\n"))
    getankte_liter = float(input("Getankte Liter:\n"))
    aktueller_spritpreis = float(input("Aktueller Spritpreis:\n"))
     
    verbrauch = (getankte_liter / gefahrene_km) * 100
    gesamtkosten = getankte_liter * aktueller_spritpreis
    reine_kosten = gesamtkosten - (verbrauch * 0.1)  # Beispiel für eine Berechnung der reinen Kosten
   
    print("Verbrauch:", verbrauch, "Liter pro 100 Kilometer")
    print("Gesamtkosten:", gesamtkosten, "Euro")
    print("Reine Kosten:", reine_kosten, "Euro")
    
    if gesamtkosten > 50.0:
        print("Die Fahrt ist zu teuer! Reise nicht antreten und lieber Bahn fahren.")
    else:
        print("Die Kosten sind in Ordnung. Gute Reise!")
