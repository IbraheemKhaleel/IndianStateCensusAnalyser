import pytest

from main_census_analyser.census_analyser_exception import WrongFilePathError, WrongExtensionCSVFile

INDIA_STATE_CENSUS_PATH = 'C:/Users/Ibrahim Khaleel/PycharmProjects/IndianStateCensusAnalyser/test_indian_state_census_analyser/IndiaStateCensusData.csv'
WRONG_CSV_PATH = 'C:/Users/Ibrahim Khaleel/PycharmProjects/test_indian_state_census_analyser/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = 'C:/Users/Ibrahim Khaleel/PycharmProjects/IndianStateCensusAnalyser/test_indian_state_census_analyser/IndiaStateCensusData.json'
INDIA_STATE_CODE_PATH = 'C:/Users/Ibrahim Khaleel/PycharmProjects/IndianStateCensusAnalyser/test_indian_state_census_analyser/IndiaStateCode.csv'
WRONG__STATE_CODE_CSV_PATH = 'C:/Users/Ibrahim Khaleel/PycharmProjects/IndianStateCensusAnalyser/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = 'C:/Users/Ibrahim Khaleel/PycharmProjects/IndianStateCensusAnalyser/test_indian_state_census_analyser/IndiaStateCode.json'


def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 29


def test_wrong_filepath_when_analysed_should_raise_errors(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG_CSV_PATH)


def test_wrong_file_extension_when_analysed_should_raise_errors(instance_of_main_class):
    with pytest.raises(WrongExtensionCSVFile):
        instance_of_main_class.load_census_data(WRONG_FILE_EXTENSION)


def test_load_state_code_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CODE_PATH)
    assert count_of_entries == 37


def test_wrong_state_code_filepath_when_analysed_should_raise_errors(instance_of_main_class):
    with pytest.raises(WrongFilePathError):
        instance_of_main_class.load_census_data(WRONG__STATE_CODE_CSV_PATH)


def test_wrong_state_code_file_extension_when_analysed_should_raise_errors(instance_of_main_class):
    with pytest.raises(WrongExtensionCSVFile):
        instance_of_main_class.load_census_data(WRONG_STATE_CODE_FILE_EXTENSION)
