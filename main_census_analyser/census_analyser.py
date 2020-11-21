import csv
import logging
import re

from main_census_analyser.census_analyser_exception import WrongFilePathError, WrongExtensionCSVFile


class StateCensusAnalyser:
    logging.basicConfig(filename='state_census_analyser.log', level=logging.DEBUG, format='%(name)s | %(levelname)s | %(asctime)s | %(message)s' )
    state_census_list = []

    def extension_validator(self, csv_file_path):
        """

        :param csv_file_path: the path of the csv file given by user
        :if it is not a csv file, this will raise an error
        """
        if not csv_file_path.endswith(".csv"):
            logging.error(' Exception occurred due to wrong file extension', exc_info=True)
            raise WrongExtensionCSVFile(' Please correct extension file')

    def load_census_data(self, file_name_path):
        """
        :param file_name_path: the state census data csv file path
        :return: count of entries inside it except heading
        """
        self.extension_validator(file_name_path)
        try:
            with open(file_name_path, 'r') as data:
                for line in csv.reader(data):
                    self.state_census_list.append(line)
                count = len(self.state_census_list)
                logging.debug('Number of entries {}'.format(count - 1))
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise WrongFilePathError('Please choose correct file path')
        return count - 1
