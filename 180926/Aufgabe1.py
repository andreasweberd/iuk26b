def berechne_bild_bits(breite, hoehe, farbtiefe):
    return breite * hoehe * farbtiefe


def bits_to_bytes(bits):
    return bits / 8


def bits_to_kibibytes(bits):
    return bits_to_bytes(bits) / 1024


def bits_to_mebibytes(bits):
    return bits_to_kibibytes(bits) / 1024


if __name__ == "__main__":
    breite = 1025
    hoehe = 680
    farbtiefe = 16

    bildgroesse = berechne_bild_bits(breite, hoehe, farbtiefe)
    print(f'Die Bildgröße beträgt: {bildgroesse} Bits.')
    print(f'Die Bildgröße beträgt: {bits_to_bytes(bildgroesse)} Bytes.')
    print(f'Die Bildgröße beträgt: {bits_to_kibibytes(bildgroesse)} KiB.')
    print(f'Die Bildgröße beträgt: {bits_to_mebibytes(bildgroesse)} MiB.')
