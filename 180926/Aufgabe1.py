def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes
def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_bytes = audio_bits / 8
    kibibytes = audio_bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes
if __name__ == "__main__":
    ergebnis_bild = berechne_bild(1025,680,16)
    print(f"Die Dateigroeße ist {ergebnis_bild} Mebibytes")
    ergebnis_audio = berechne_audio(44100,16,2,10)
    print(f"Die Audiodateigroeße ist {ergebnis_audio} Mebibytes")

