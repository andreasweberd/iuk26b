def berechne_bild(breite, hoehe, farbtiefe):
    groesse = breite * hoehe * farbtiefe    # Bits
    groesse /= 8                            # Bytes
    groesse /= 1024 ** 2                    # Mebibytes
    return groesse

def berechne_audio(abtastrate, bittiefe, kanaele, zeit):
    groesse = abtastrate * bittiefe * kanaele * zeit    # bits
    groesse /= 8 * (1024 ** 2)                          # Mebibytes
    return groesse

if __name__ == "__main__":
    bild_groesse_mebibytes = round(berechne_bild(1025, 680, 16), 2)
    audio_groesse_mebibytes = round(berechne_audio(44100, 16, 2, 10), 2)
    print(f"Das Bilddatei nimmt {bild_groesse_mebibytes} MiBs Speicherplatz ein.\nDie Audiodatei nimmt {audio_groesse_mebibytes} MiBs Speicherplatz ein.")
