def tuetwas():
    gefahrene_km = float(input("km als zahl (zB 6.7)\n"))
    getankte_liter = float(input("liter als zahl (zB 6.7)\n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100

    print(f"Der Verbrauch lag bei mir {verbrauch} pro 100km.")

    if verbrauch > 8:
        print("Verbrauch ist zu hoch")

    else:
        print("Verbrauch ist angemessen")

if __name__=="__main__":
    tuetwas()
