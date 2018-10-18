from enum import Enum


class TerminalBackspaceKeyMode(Enum):
    Default = 0
    ControlH = 1
    ControlQuestionMark = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalBackspaceKeyMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalBackspaceKeyMode]
        return int_value in values
