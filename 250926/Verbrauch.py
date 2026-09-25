def Verbrauch():
    while True:
        Kilometer = input("Wieviele Kilometer sind Sie gefahren? ")
        if Kilometer.isdigit == False:
            continue
        else:
            Kilometer = int(Kilometer)
            break
    while True:
        Liter = input("Wieviele Liter haben Sie dabei Verbraucht? ")
        if Liter.isdigit == False:
            continue
        else:
            Liter = int(Liter)
            break
    Verbrauch = (Liter * Kilometer) / 100
    print(f"Ihr Verbrauch beträgt {Verbrauch}L/100km")
    if Verbrauch > 8 == True:
        print("Hoher Verbrauch!")
    elif Verbrauch > 8 == False:
        print("Sparsame")

if __name__ == "__main__":
    Verbrauch()