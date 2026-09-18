def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    # Kibibits = Bits / 1024
    # Kibibytes = Kibibits / 8
    Mebibytes = Kibibytes / 1024
    print(Bits)
    # print(Kibibits)
    print(Kibibytes)
    print(Mebibytes)

if __name__ == "__main__":
    berechne_bild(1025, 680, 16)