def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes
if __name__ == "__main__":
    ergebnis = berechne_bild(1025,680,16)
    print(f"Die Dateigroeße ist {ergebnis}")