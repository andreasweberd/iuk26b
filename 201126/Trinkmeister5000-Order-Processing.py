inventory = [3,5,7,2,4,6,8,4,2,5]
preise = {1: 1.5, 2:  2.0, 3: 1.0, 4: 4.7, 5: 3.3, 6: 1.75, 7: 0.99, 8: 1.69, 9: 3.25, 10: 1.23}

def process_client_order(product_id):
    einwurfbetrag = 0
    preis = preise[product_id]
    if inventory[product_id - 1] > 0:
        while einwurfbetrag < preis:
            einwurfbetrag += float(input(f"\nPreis: {preis}\nEingeworfen: {einwurfbetrag}\nMuenze einwerfen (z.B. 0.5 für 50 Cent): "))
        print(f"Rückgeld: {einwurfbetrag - preis}\n*Produkt wird ausgegeben*")
    else:
        print("Das Produkt ist nicht auf Lager")

process_client_order(1)