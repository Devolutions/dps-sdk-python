from enum import Enum


class DefaultBoolean(Enum):
    Default = 0
    true = 1
    false = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in DefaultBoolean.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DefaultBoolean]
        return int_value in values
