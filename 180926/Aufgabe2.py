def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
    groesse_bits = abtastrate * bittiefe * kanaele * zeit_in_sekunden
    groesse_mib = groesse_bits / 8 / 1024 / 1024
    print(f"Die Audiodatei hat eine Größe von {groesse_mib} MiB")

if __name__ == "__main__":
    berechne_audio(44100, 16, 2, 10)