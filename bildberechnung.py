# berechne_bild(breite, hoehe, farbtiefe)
# Dateigröße zuerst in Bits berechnen
# Bits in Mebibyte (MiB) umrechnen
# Funktion in main mit Werten aufrfen - Breite 1025, Höhe 680, Farbtiefe 16 Bits
# Ergebnis mit print() ausgeben lassen

def berechne_bild(breite, hoehe, farbtiefe):
    bits 		= 	breite * hoehe * farbtiefe
    bytes 		= 	bits 		/ 	8
    kibibytes 	= 	bytes 		/ 	1024
    mebibytes 	= 	kibibytes 	/ 	1024
    
    return mebibytes

if __name__ == "__main__":
    ergebnis = berechne_bild(1025, 680, 16)
    print(f"Die Dateigröße ist {ergebnis}")