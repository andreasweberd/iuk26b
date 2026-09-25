#def tuwtwas():
#    gefahrene_km = float(input("Gefahrene Kilometer:\n"))
#    getankte_liter = float(input("Getankte Liter:\n"))
#    verbrauch = (getankte_liter / gefahrene_km) * 100
#    print("Verbrauch:", verbrauch, "Liter pro 100 Kilometer")
#    print(f"Der Verbrauch lag bei {verbrauch} Liter pro 100 Kilometer.")
#    if verbrauch > 8:
#        print("Hoher Verbrauch.")
#    else:
#        print("Sparsamer Verbrauch.")


if __name__ == "__main__":
    
    gefahrene_km = float(input("Gefahrene Kilometer:\n"))
    getankte_liter = float(input("Getankte Liter:\n"))
     
    verbrauch = (getankte_liter / gefahrene_km) * 100
    print("Verbrauch:", verbrauch, "Liter pro 100 Kilometer")
#    print(f"Der Verbrauch lag bei {verbrauch} Liter pro 100 Kilometer.")
    
    if verbrauch > 8:
        print("Hoher Verbrauch.")
    else:
        print("Sparsamer Verbrauch.")

#    tuwtwas()