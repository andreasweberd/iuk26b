def berechne_bild(breite, hoehe, farbtiefe):
        groesse_bits = float(breite * hoehe * farbtiefe)
        groesse_mib = groesse_bits / 8 / 1024 / 1024
        print(f"Das Bild hat eine Größe von {groesse_mib} MiB.")

  

def berechne_audio(abtastrate, bittiefe, kanaele, zeit_in_sekunden):
        groesse = float(abtastrate * bittiefe * kanaele * zeit_in_sekunden)
        groesse_m = groesse / 8 / 1024 / 1024 
        print(f"Die Datei ist { groesse_m} mib groß")


 
if __name__ == "__main__":
        berechne_bild(1025, 680, 16) 
        berechne_audio(44100, 16, 2, 10)
 