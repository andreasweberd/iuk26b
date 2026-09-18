def berechne_bild(breite, hoehe, farbtiefe):
    bits = breite * hoehe * farbtiefe
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    
    return mebibytes

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    audio_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    audio_bytes = audio_bits / 8
    audio_kibibytes = audio_bytes / 1024
    audio_mebibytes = audio_kibibytes / 1024
    
    return audio_mebibytes

if __name__ == "__main__":
    ergebnis = berechne_bild(1025, 680, 16)
    audio_ergebnis = berechne_audio(44100, 16, 2, 10)
    print(f"Die Datei ist {ergebnis} MiB und die Audiodatei ist {audio_ergebnis} MiB groß.")

    
    
