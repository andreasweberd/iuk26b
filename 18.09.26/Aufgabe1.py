def berechne_bild(breite, hoehe, farbtiefe):
    groesse = breite * hoehe * farbtiefe # Bits
    groesse /= 8 # Bytes
    groesse /= 1024 ** 2 # Mebibytes
    return groesse

if __name__ == "__main__":
    bild_groesse_mebibytes = round(berechne_bild(1025, 680, 16), 2)
    print(f"Das Bild nimmt {bild_groesse_mebibytes} MiBs Speicher ein.")
