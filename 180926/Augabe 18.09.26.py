
def berechne_bild(breite, höhe,farbtiefe):
bits = breite * hoehe * farbtiefe
bytes = bits / 8
kibibytes = bytes / 1024
mibibytes = kibibytes / 1024

return bits

if__name__ == "__main__":
ergebins = berechne_bild(1025, 680, 116)
print(f"Die dateigröße ist {ergebins}")