from enum import Enum


class ScreenSize(Enum):
    Default = 0
    FullScreen = 1
    R640x480 = 2
    R800x600 = 3
    R1024x768 = 4
    R1152x864 = 5
    R1280x800 = 6
    R1280x1024 = 7
    R1440x900 = 8
    R1400x1050 = 9
    R1600x1024 = 10
    R1600x1200 = 11
    R1600x1280 = 12
    R1680x1050 = 13
    R1900x1200 = 14
    R1920x1200 = 15
    R2048x1536 = 16
    R2560x2048 = 17
    R3200x2400 = 18
    R3840x2400 = 19
    Custom = 20
    CurrentScreenSize = 21
    CurrentWorkAreaSize = 22

    @staticmethod
    def value_from_name(typename):
        for name, member in ScreenSize.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ScreenSize]
        return int_value in values
