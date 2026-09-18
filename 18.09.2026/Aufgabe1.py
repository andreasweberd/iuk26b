#Die Bild-Berechnung:
#1. Schreibe eine Funktion mit dem Namen berechne_bild(breite, hoehe, farbtiefe)
#2. Berechne innerhalb der Funktion die Dateigröße zuerst in Bits (Breite x Höhe x Farbtiefe)
#3. Rechne die Bits anschließend in Mebibyte (MB) um.
#4. Rufe die Funktion in main mit Werten auf. Bildbreite 1025, Bildhöhe 680, Farbtiefe 16 Bits
#5. Gib das Ergebnis mit einem schönen Satz über print() auf der Konsole aus.

def berechnen_bild (breite, hoehe, farbtiefe):
    breite = 1025
    hoehe = 680 
    farbtiefe = 16
    bite = breite * hoehe * farbtiefe 
    bytes = bite / 8
    kibibyte = bytes / 1024
    mebibyte = kibibyte / 1024
    return mebibyte

if __name__ == "__main__":
    Ergebnis = berechnen_bild(1025, 680, 16)
    bildgroesse = Ergebnis 
    print (f"Die berechnete Bildgröße beträgt {bildgroesse} MB.")



