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
    mebibyte_bild = kibibyte / 1024
    return mebibyte_bild

def berechne_audio (abtastrate, bittiefe, kaneale, zeit):
    abtastrate = 44100
    bittiefe = 16
    kaneale = 2
    zeit = 10
    bite = abtastrate * bittiefe * kaneale * zeit
    bytes = bite / 8
    kibibyte = bytes / 1024
    mebibyte_audio = kibibyte / 1024
    return mebibyte_audio

if __name__ == "__main__":
    Ergebnis = berechnen_bild(1025, 680, 16)
    bildgroesse = Ergebnis 
    print (f"Die berechnete Bildgröße beträgt {bildgroesse} MB.")

    
    audiogroesse = berechne_audio(44100, 16, 2, 10) 
    print (f"Die berechnete Audiogöße beträgt {audiogroesse} MB.")
    