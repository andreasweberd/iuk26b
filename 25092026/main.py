def tuetwas():
    gefahrene_km = float(input("wie viele gefahrene km (als zahl): \n"))
    getankte_liter = float(input("getankte Liter (als zahl): \n"))

    verbrauch = (getankte_liter / gefahrene_km) * 100

    print(f"der verbrauch liegt bei {verbrauch} pro 100 km")

    if verbrauch > 8:
        print("verbrauch leider zu hoch")
    else:
        print("verbrauch sehr sparsam")

    gesamtkosten = reisekosten(getankte_liter, gefahrene_km, verbrauch)

    print(f" die reisekosten liegen bei {gesamtkosten} $" )



def reisekosten(getankte_liter, gefahrene_km, verbrauch):
    sprit_preis = 2.45;
    gesamtkosten = getankte_liter * sprit_preis
    return gesamtkosten





if __name__ == '__main__':
    tuetwas()



