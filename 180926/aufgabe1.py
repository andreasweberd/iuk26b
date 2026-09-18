def berechne_bild(breite, hoehe, farbtiefe):
        groesse_bits = float(breite * hoehe * farbtiefe)
        groesse_mib = groesse_bits / 8 / 1024 / 1024
        print(f"Das Bild hat eine Größe von {groesse_mib} MiB.")
 
berechne_bild(1025, 680, 16)
 
if __name__ == "__main__":
        berechne_bild(1025, 680, 16)
 