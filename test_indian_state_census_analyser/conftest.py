import pytest

from main_census_analyser.census_analyser import StateCensusAnalyser


@pytest.fixture
def instance_of_main_class():
    state_census_analyser = StateCensusAnalyser()
    return state_census_analyser
