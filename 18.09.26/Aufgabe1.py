def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    anzahl_bytes = bits / 8
    kibibytes = anzahl_bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_anzahl_bytes = audio_bits / 8
    audio_kibibytes = audio_anzahl_bytes / 1024
    audio_mebibytes = audio_kibibytes / 1024
    return audio_mebibytes


if __name__ == "__main__":
    ergebnis = berechne_bild(1025, 680, 16)
    audio_ergebnis = berechne_audio(44100, 16, 2, 10)
    print(f"Die Dateigröße ist {ergebnis:.2} MiB und die Audiodateigröße ist {audio_ergebnis:.2} MiB groß.")
