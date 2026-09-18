class BitConverter():

    def __init__(self, type, value):

        if type not in ['bits', 'bytes', 'kibibytes', 'mebibytes']:
            raise ValueError(
                "Ungültiger Typ. Erlaubte Typen: 'bits', 'bytes', 'kibibytes', 'mebibytes'.")

        if type == 'bits':
            self.__bits = value
            self.__bytes = self.__bits_to_bytes(value)
            self.__kibibytes = self.__bits_to_kibibytes(value)
            self.__mebibytes = self.__bits_to_mebibytes(value)

        elif type == 'bytes':
            self.__bytes = value
            self.__bits = value * 8
            self.__kibibytes = self.__bits_to_kibibytes(self.__bits)
            self.__mebibytes = self.__bits_to_mebibytes(self.__bits)

    def __bits_to_bytes(self, bits):
        return bits / 8

    def __bits_to_kibibytes(self, bits):
        return self.__bits_to_bytes(bits) / 1024

    def __bits_to_mebibytes(self, bits):
        return self.__bits_to_kibibytes(bits) / 1024

    def get_bits(self):
        return self.__bits

    def get_bytes(self):
        return self.__bytes

    def get_kibibytes(self):
        return self.__kibibytes

    def get_mebibytes(self):
        return self.__mebibytes
