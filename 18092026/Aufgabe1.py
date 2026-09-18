def main():

    def berechne_bildbreite(breite:int, hoehe:int ,farbtiefe:int):
        # Die 8.388.608 entsteht durch die Multiplikation von 8 und 1024^2
        # Die Größe wird somit direkt in MiB berechnet
        return (breite * hoehe * farbtiefe)  / 8388608

    def berechne_audio(abtastrate, bittiefe:int, kanaele, zeit):
        # Die 8.388.608 entsteht durch die Multiplikation von 8 und 1024^2
        # Die Größe wird somit direkt in MiB berechnet
        return (abtastrate*bittiefe*kanaele*zeit) / 8388608

    # Bild
    print (f"Der benötigte Speicher für dieses Bild beträgt {berechne_bildbreite(1025,680,16)}MiB")
    # Audio
    print (f"Der benötigte Speicher für diese Audio beträgt {berechne_audio(44100,16,2,10)}MiB")

if __name__ == "__main__":
    main()