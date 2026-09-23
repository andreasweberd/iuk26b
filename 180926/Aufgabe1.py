import BitConverter as bc


def berechne_bild_bits(breite, hoehe, farbtiefe):
    return breite * hoehe * farbtiefe


def berechne_audio_bits(abtastrate, bit_tiefe, kanal_anzahl, zeit_in_sekunden):
    return abtastrate * bit_tiefe * kanal_anzahl * zeit_in_sekunden


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

    abtastrate = 44100
    bit_tiefe = 16
    kanal_anzahl = 2
    zeit_in_sekunden = 10

    bildgroesse_bits = berechne_bild_bits(breite, hoehe, farbtiefe)
    audio_bits = berechne_audio_bits(
        abtastrate, bit_tiefe, kanal_anzahl, zeit_in_sekunden)

    bildgroesse = bc.BitConverter("bits", bildgroesse_bits)
    audio_bits = bc.BitConverter("bits", audio_bits)
    print(f'Die Bildgröße beträgt: {bildgroesse.get_bits()} Bits.')
    print(
        f'oder {bildgroesse.get_bytes()} Bytes.')
    print(
        f'oder {bildgroesse.get_kibibytes()} KiB.')
    print(
        f'oder {bildgroesse.get_mebibytes()} MiB.')

    print(f'Die Audiogröße beträgt: {audio_bits.get_bits()} Bits')

    print(f'oder {audio_bits.get_mebibytes()} Mebibytes')
