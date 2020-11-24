import enum


class ExceptionType(enum.Enum):
    """
    Created an exception class with enums for different errors
    """

    WrongFilePathError = "Path of file is incorrect "
    WrongExtensionCSVFile = "Extension of file is wrong"
    WrongHeader = "Heading is corrupted"
    WrongDelimiter = "Error occurred in delimiter matching"


class CensusAnalyserError(Exception):

    def __init__(self, *args):

        self.type = args[0]
        self.message = args[1]
