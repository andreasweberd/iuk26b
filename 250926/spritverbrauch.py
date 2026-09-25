
if __name__ == "__main__":

    gefahrene_km = float(input("km als zahl\n"))
    getankte_liter = float(input("l als zahl\n"))


    verbrauch = float(getankte_liter / gefahrene_km) * 100

    print(f"der verbrauch ist {verbrauch} ")

    if verbrauch >8:
        print("der varbrauch ist zu hoch ")

    else: 
        print("verbrauch ist gut")
    