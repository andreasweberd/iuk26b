
def berechne_bild(breite,hoehe,tiefe):
    bits = breite * tiefe * hoehe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes



if __name__ == "__main__":

    ergebnis = berechne_bild(1025,680,16)
    print(f" Die Dateigröße ist {ergebnis}")
