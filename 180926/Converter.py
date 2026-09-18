class Converter():

    def __init__(self, type, bits):
        self.__type = type
        self.__bits = bits
        self.__bytes = self.bits_to_bytes(bits)
        self.__kibibytes = self.bits_to_kibibytes(bits)
        self.__mebibytes = self.bits_to_mebibytes(bits)

    def bits_to_bytes(self, bits):
        return bits / 8

    def bits_to_kibibytes(self, bits):
        return self.bits_to_bytes(bits) / 1024

    def bits_to_mebibytes(self, bits):
        return self.bits_to_kibibytes(bits) / 1024
