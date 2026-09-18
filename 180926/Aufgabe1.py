def berechne_bild(breite, hoehe, farbtiefe):
    Bits = breite * hoehe * farbtiefe
    Bytes = Bits / 8
    Kibibytes = Bytes / 1024
    Mebibytes = Kibibytes / 1024
    return Mebibytes

def berechne_audio(abtastrate, bittiefe, kanaele, sekunden):
    Audio_Bits = abtastrate * bittiefe * kanaele * sekunden
    Audio_Bytes = Audio_Bits / 8
    Audio_Kibibytes = Audio_Bytes / 1024
    Audio_Mebibytes = Audio_Kibibytes / 1024
    return Audio_Mebibytes

if __name__ == "__main__":
    ergebnis = berechne_bild(1025, 680, 16)
    audio_ergebnis = berechne_audio(44100, 16, 2, 10)
    print(f"Die Bilddatei ist {ergebnis} Mebibytes groß und die Audiodatei ist {audio_ergebnis} Mebibytes groß")

# def berechne_bild(breite, hoehe, farbtiefe):
#     Bits = breite * hoehe * farbtiefe
#     bitsUmrechner(Bits)

# def berechne_audio(abtastrate, bittiefe, kanaele, sekunden):
#     Bits = abtastrate * bittiefe * kanaele * sekunden
#     bitsUmrechner(Bits)

# def bitsUmrechner(Bits):
#     Bytes = Bits / 8
#     Kibibytes = Bytes / 1024
#     Mebibytes = Kibibytes / 1024
#     print(f"Die ursprünglichen {Bits} Bits sind umgerechnet {Mebibytes}")

# if __name__ == "__main__":
#     berechne_bild(1025, 680, 16)
#     berechne_audio(44100, 16, 2, 10)