from enum import Enum


class AzureMFAMode(Enum):
    Sms = 0
    PhoneCall = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in AzureMFAMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in AzureMFAMode]
        return int_value in values
