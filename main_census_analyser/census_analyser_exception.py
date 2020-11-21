class CensusAnalyserException(Exception) :
    def __init__(self, message):
        super().__init__(message)


class WrongFilePathError(CensusAnalyserException):
    pass


class WrongExtensionCSVFile(CensusAnalyserException):
    pass
