from enum import Enum


class DocumentConnectionType(Enum):
    Default = 0
    Word = 1
    Excel = 2
    PowerPoint = 3
    Image = 4
    Visio = 5
    OneNote = 6
    PDF = 7
    Certificate = 8
    Text = 9
    PhoneBook = 10
    PrivateKey = 11
    Email = 12
    Spreadsheet = 13
    RichText = 14
    Video = 15
    Html = 16
    HtmlEditor = 17
    DataSourceConfiguration = 18
    TextPlain = 19

    @staticmethod
    def value_from_name(typename):
        for name, member in DocumentConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DocumentConnectionType]
        return int_value in values
