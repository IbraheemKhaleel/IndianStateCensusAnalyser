import pytest

from main_census_analyser.census_analyser_exception import CensusAnalyserError

INDIA_STATE_CENSUS_PATH = '../test_indian_state_census_analyser/IndiaStateCensusData.csv'
WRONG_CSV_PATH = '../wrong_path/test_indian_state_census_analyser/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '../test_indian_state_census_analyser/IndiaStateCensusData.json'
WRONG_DELIMITER_CENSUS_PATH = '../test_indian_state_census_analyser/DelimiterIndiaCensusCode.csv'
MISSING_HEADER_CENSUS_PATH = '../test_indian_state_census_analyser/MissingHeaderCensusCode.csv'
INDIA_STATE_CODE_PATH = '../test_indian_state_census_analyser/IndiaStateCode.csv'
WRONG__STATE_CODE_CSV_PATH = '../IndianStateCensusAnalyser/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '../test_indian_state_census_analyser/IndiaStateCode.json'
MISSING_HEADER_STATE_CODE_PATH = '../test_indian_state_census_analyser/MissingHeaderIndiaStateCode.csv'
WRONG_DELIMITER_STATE_CODE_PATH = '../test_indian_state_census_analyser/DelimiterIndiaStateCode.csv'


def test_load_census_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CENSUS_PATH)
    assert count_of_entries == 29


@pytest.mark.parametrize("path_of_file, expected",
                         [(WRONG_CSV_PATH, CensusAnalyserError),
                          (WRONG_FILE_EXTENSION, CensusAnalyserError),
                          (WRONG_DELIMITER_CENSUS_PATH, CensusAnalyserError),
                          (MISSING_HEADER_CENSUS_PATH, CensusAnalyserError)])
def test_wrong_filepath_when_analysed_should_raise_errors(path_of_file, expected, instance_of_main_class):
    with pytest.raises(expected):
        instance_of_main_class.load_census_data(path_of_file)


def test_load_state_code_data(instance_of_main_class):
    count_of_entries = instance_of_main_class.load_census_data(INDIA_STATE_CODE_PATH)
    assert count_of_entries == 37


@pytest.mark.parametrize("path_of_file, expected", [(WRONG__STATE_CODE_CSV_PATH, CensusAnalyserError),
                                                    (WRONG_STATE_CODE_FILE_EXTENSION, CensusAnalyserError),
                                                    (MISSING_HEADER_STATE_CODE_PATH, CensusAnalyserError),
                                                    (WRONG_DELIMITER_STATE_CODE_PATH, CensusAnalyserError)
                                                    ])
def test_wrong_state_code_filepath_when_analysed_should_raise_errors(path_of_file, expected, instance_of_main_class):
    with pytest.raises(expected):
        instance_of_main_class.load_census_data(path_of_file)


def test_sorting_datas_by_state(instance_of_main_class):
    state_name = instance_of_main_class.sorting_datas_by_state(INDIA_STATE_CENSUS_PATH)
    assert state_name[0]['State'] == "Andhra Pradesh"


def test_sorting_datas_by_last_state(instance_of_main_class):
    state_name = instance_of_main_class.sorting_datas_by_state(INDIA_STATE_CENSUS_PATH)
    assert state_name[len(state_name) - 1]['State'] == "West Bengal"


def test_sorting_datas_by_first_state_code(instance_of_main_class):
    state_code = instance_of_main_class.sorting_datas_by_state_code(INDIA_STATE_CODE_PATH)
    assert state_code[0]['StateCode'] == "AD"


def test_sorting_datas_by_last_state_code(instance_of_main_class):
    state_code = instance_of_main_class.sorting_datas_by_state_code(INDIA_STATE_CODE_PATH)
    assert state_code[len(state_code) - 1]['StateCode'] == "WB"


def test_sort_by_largest_area(instance_of_main_class):
    largest_area = instance_of_main_class.sort_by_area(INDIA_STATE_CENSUS_PATH)
    assert largest_area[0]['AreaInSqKm'] == "342239"


def test_sort_by_population_density(instance_of_main_class):
    largest_population_density = instance_of_main_class.sort_by_population_density(INDIA_STATE_CENSUS_PATH)
    assert largest_population_density[0].get('DensityPerSqKm') == "1102"


def test_sort_by_population(instance_of_main_class):
    largest_population = instance_of_main_class.sort_by_population(INDIA_STATE_CENSUS_PATH)
    assert largest_population[0].get('Population') == "199812341"
