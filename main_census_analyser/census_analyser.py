import csv
import json
import logging

from main_census_analyser.census_analyser_exception import CensusAnalyserError, ExceptionType

logging.basicConfig(filename='state_census_analyser.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')


class StateCensusAnalyser:
    census_list = []

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
                for row in csv_reader_file:
                    census_dictionary = {}
                    for key in row:
                        census_dictionary[key] = row.get(key)
                    self.census_list.append(census_dictionary)
                logging.debug("Number of entries are {}".format(len(self.census_list)))
        except FileNotFoundError:
            logging.exception("Please choose a correct path")
            raise CensusAnalyserError(ExceptionType.WrongFilePathError, "Path of file is incorrect")
        return len(self.census_list)

    def list_to_json_format(self, sorted_datas):
        """
        Creating method to convert python format to json  format
        :param sorted_datas: The sorted python datas of respectve fields
        """
        sorted_list = []
        for _ in sorted_datas:
            sorted_list.append(json.dumps(_))

    def sorting_datas_by_state(self, file_name_path):
        """
        Creating methods to sort state name
        :param file_name_path: the path of the csv file to sort the elements in state name wise
        :return: first and last state in alphabetical order
        """
        self.load_census_data(file_name_path)
        sorted_datas = sorted(self.census_list, key=lambda a: a['State'])
        self.list_to_json_format(sorted_datas)
        logging.debug(
            "first state is {} and last state is {}".format(sorted_datas[0]['State'], sorted_datas[28]['State']))
        return sorted_datas

    def sort_by_population(self, file_name_path):
        """
        Creating method to sort states with respect to their population in descending order
        :param file_name_path: the path of the csv file to sort the elements in population wise
        :return: most populous state
        """
        self.load_census_data(file_name_path)
        sorted_data = sorted(self.census_list, key=lambda b: int(b.get('Population')), reverse=True)
        with open('descending_order_most_populous_stae.json', 'w') as file:
            json.dump(sorted_data, file, indent=5)
        logging.debug("The most populous state is {}".format(sorted_data[0]['Population']))
        return sorted_data

    def sorting_datas_by_state_code(self, file_name_path):
        """
        Creating method to sort elements by state code
        :param file_name_path: the path of the csv file to sort the elements in state code wise
        :return: first and last state codes in alphabetical wise
        """
        self.load_census_data(file_name_path)
        sorted_datas = sorted(self.census_list, key=lambda b: b['StateCode'])
        self.list_to_json_format(sorted_datas)
        logging.debug("first state code is {} and last state code is {}".format(sorted_datas[0]['StateCode'],
                                                                                sorted_datas[len(sorted_datas) - 1][
                                                                                    'StateCode']))
        return sorted_datas

    def sort_by_population_density(self, file_name_path):
        """

        :param file_name_path: the path of the csv file to sort the elements in population density wise
        :return: most populous and least populous state

        """
        self.load_census_data(file_name_path)
        sorted_data = sorted(self.census_list, key=lambda b: int(b.get('DensityPerSqKm')), reverse=True)
        with open('descending_order_populous_states.json', 'w') as file:
            json.dump(sorted_data, file, indent=5)
        logging.debug("Most densly populated state".format(sorted_data[0]['DensityPerSqKm']))
        return sorted_data

    def sort_by_area(self, file_name_path):
        """
        Creating a method to give the largest area state
        :param file_name_path: the path of the csv file to sort the elements in area wise
        :return: largest area state
        """
        self.load_census_data(file_name_path)
        sorted_data = sorted(self.census_list, key=lambda b: int(b.get('AreaInSqKm')), reverse=True)
        with open('descending_order_area_states.json', 'w') as file:
            json.dump(sorted_data, file, indent=5)
        logging.debug("The largest area state is {}".format(sorted_data[0]['AreaInSqKm']))
        return sorted_data
