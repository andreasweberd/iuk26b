
def berechne_bild(breite, höhe,farbtiefe):
    bits = breite * höhe * farbtiefe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mibibytes = kibibytes / 1024

    return mibibytes


def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    #Audiobit-Bits berechnen: abstrate * bittiefe * kanaele * zeit
    audio_bits= abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_bytes   = audio_bits / 8
    audio_kibibytes = audio_bytes / 1024
    audio_mebibytes = audio_kibibytes / 1024

    return audio_mebibytes

if __name__ == "__main__":
    ergebins = berechne_bild(1025, 680, 16)
    print(f"Die Bild Datei ist {ergebins} groß")
    ergebins = berechne_audio(44100, 16, 2, 10)
    print(f"Die Audio Datei ist {ergebins} groß")


