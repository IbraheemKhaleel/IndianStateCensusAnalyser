import csv
import json
import logging
from collections import OrderedDict

from main_census_analyser.census_analyser_exception import CensusAnalyserError, ExceptionType

logging.basicConfig(filename='state_census_analyser.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')


class StateCensusAnalyser:
    ordered_census_dictionary = OrderedDict()

    def validate_csv_file(self, csv_file_path):
        self.extension_validator(csv_file_path)
        self.validate_header(csv_file_path)
        self.validate_delimiter(csv_file_path)

    def extension_validator(self, csv_file_path):
        """

        :param csv_file_path: the path of the csv file given by user
        :if it is not a csv file, this will raise an error
        """
        if not csv_file_path.endswith(".csv"):
            logging.error(' Exception occurred due to wrong file extension', exc_info=True)
            raise CensusAnalyserError(ExceptionType.WrongExtensionCSVFile, "Extension of file is wrong")

    def validate_delimiter(self, csv_file_path):
        with open(csv_file_path, newline="") as csv_data:
            try:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
            except:
                logging.exception("Delimiter is invalid")
                raise CensusAnalyserError(ExceptionType.WrongDelimiter, "Error occurred in delimiter matching")

    def validate_header(self, csv_file_path):
        with open(csv_file_path, newline="") as csv_data:
            if not csv.Sniffer().has_header(csv_data.read()):
                logging.error("Improper header", exc_info=True)
                raise CensusAnalyserError(ExceptionType.WrongHeader, "Heading is corrupted")

    def load_census_data(self, file_name_path):
        """
        :param file_name_path: the state census data csv file path
        :return: count of entries inside it except heading
        """
        try:
            self.validate_csv_file(file_name_path)
            with open(file_name_path, mode='r') as data:
                csv_reader_file = csv.DictReader(data)
                count = 0
                for row in csv_reader_file:
                    count += 1
                    self.ordered_census_dictionary[count] = {}
                    for key in row:
                        self.ordered_census_dictionary[count][key] = row.get(key)
                logging.debug("Number of entries are {}".format(count))
                print(self.ordered_census_dictionary)
        except FileNotFoundError:
            logging.exception("Please choose a correct path")
            raise CensusAnalyserError(ExceptionType.WrongFilePathError, "Path of file is incorrect")
        return count

    def sorting_datas_by_state(self, file_name_path):
        """

        :param file_name_path: the path of the csv file to sort the elements in state name wise
        :return: first and last state in alphabetical order
        """
        self.load_census_data(file_name_path)
        sorted_datas = sorted(self.ordered_census_dictionary.items(), key=lambda a: a[1]['State'])
        sorted_list = []
        for _ in sorted_datas:
            sorted_list.append(json.dumps(_[1]))
        logging.debug("first state is {} and last state is {}".format(sorted_datas[0][1]['State'], sorted_datas[28][1]['State']))
        return sorted_datas[0][1]['State'], sorted_datas[28][1]['State']

    def sorting_datas_by_state_code(self, file_name_path):
        """

        :param file_name_path: the path of the csv file to sort the elements in state code wise
        :return: first and last state codes in alphabetical wise
        """
        self.load_census_data(file_name_path)
        sorted_datas = sorted(self.ordered_census_dictionary.items(), key= lambda b : b[1]['StateCode'])
        sorted_list = []
        for _ in sorted_datas:
            sorted_list.append(json.dumps(_[1]))
        logging.debug("first state code is {} and last state code is {}".format(sorted_datas[0][1]['StateCode'], sorted_datas[36][1]['StateCode']))
        return sorted_datas[0][1]['StateCode'], sorted_datas[36][1]['StateCode']