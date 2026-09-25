if __name__ == "__main__":
    
    gefahrene_km = input("Gefahrene Kilometer: ")
    getankte_liter = input("Getankte Liter: ")
    
    verbrauch = (float(getankte_liter) / float(gefahrene_km)) * 100
    print("Verbrauch:", verbrauch, "Liter pro 100 Kilometer")
    
    if verbrauch > 8:
        print("Hoher Verbrauch.")
    else:
        print("Sparsamer Verbrauch.")