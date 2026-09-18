def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    anzahl_bytes = bits / 8
    kibibytes = anzahl_bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes


def berechne_audio(abtastrate, bittiefe, kanaele, dauer):
    bits = abtastrate * bittiefe * kanaele * dauer
    anzahl_bytes = bits / 8
    kibibytes = anzahl_bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes


if __name__ == "__main__":
    ergebnis = berechne_bild(1025, 680, 16)
    print(f"Die Dateigroesse ist {ergebnis:.2f} Mebibyte.")

    ergebnis_audio = berechne_audio(44100, 16, 2, 180)
    print(f"Die Dateigroesse der Audiodatei ist {ergebnis_audio:.2f} Mebibyte.")
