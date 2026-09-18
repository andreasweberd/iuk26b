def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sek):
    Audio_Bits = abtastrate * bittiefe * kanaele * zeit_in_sek
    bytes = Audio_Bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes

if __name__ == '__main__':
    Bild = berechne_bild(1025, 680, 16)
    Audio = berechne_audio(44100, 16, 2, 10)
    print(f"Die Bilddatei hat eine größe von {Bild} Mebibyte")
    print(f"Die Audiodatei hat eine größe von {Audio} Mebibyte")