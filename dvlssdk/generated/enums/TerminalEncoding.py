from enum import Enum


class TerminalEncoding(Enum):
    Default = 0
    UseFontEncoding = 1
    UTF_8 = 2
    ISO_8859_1 = 3
    ISO_8859_2 = 4
    ISO_8859_3 = 5
    ISO_8859_4 = 6
    ISO_8859_5 = 7
    ISO_8859_6 = 8
    ISO_8859_7 = 9
    ISO_8859_8 = 10
    ISO_8859_9 = 11
    ISO_8859_10 = 12
    ISO_8859_11 = 13
    ISO_8859_13 = 14
    ISO_8859_14 = 15
    ISO_8859_15 = 16
    ISO_8859_16 = 17
    KOI8_U = 18
    KOI8_R = 19
    HP_ROMAN8 = 20
    VSCII = 21
    DEC_MCS = 22
    Win1250 = 23
    Win1251 = 24
    Win1252 = 25
    Win1253 = 26
    Win1254 = 27
    Win1255 = 28
    Win1256 = 29
    Win1257 = 30
    Win1258 = 31
    CP437 = 32
    CP620 = 33
    CP819 = 34
    CP852 = 35
    CP878 = 36

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalEncoding.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalEncoding]
        return int_value in values
