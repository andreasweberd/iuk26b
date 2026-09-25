if __name__ == "__main__":
    gefahrene_km = float(input("Gib die gefahrenen km an (z.B.: 148.4): "))
    liter = float(input("Gib die verbrauchten Liter an (z.B.: 10.6): "))
    verbrauch = round(liter / gefahrene_km * 100, 2)
    print(f"Der Verbrauch ist {verbrauch}L/100km -> " + ("hoch." if (verbrauch > 8) else "sparsam."))
    # ich weiß ich haette einfach ne normale if bedingung machen können aber mir war langeweilig also hab ich es komplizierter wie nötig gemacht :D