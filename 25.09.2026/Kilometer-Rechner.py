
if __name__ =="__main__":
    gefahrene_km = input(float("gefahrene kilometer angeben als zahl/n"))
    getankte_liter = input (float("getankte Liter angeben als zahl/n"))

    Verbrauch = (getankte_liter / gefahrene_km) *100

    print(f"Der Verbrauch lag bei {Verbrauch}Liter pro 100 km")

    if Verbrauch >8: 
        print("hoher Verbrauch")

    else:
        print ("geringer Verbrauch")
