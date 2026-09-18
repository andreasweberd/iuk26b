
def berechne_audio (abtastrate, bittiefe, kanaele , zeit_in_sekunden):
    bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    bytes = bits / 8
    kibibytes = bytes / 1024
    mebibytes = kibibytes / 1024
    return mebibytes

if __name__ == "__main__":
    ergebnis = berechne_audio(44100,16,2,10)
    print(f"Die Dateigröße ist {ergebnis}")
