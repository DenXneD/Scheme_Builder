from server.spring.domain.spring import Spring
from server.spring.pickle_dao import SpringDAO
from server.parser import SpringsToCodeParser
from server.springs_test import SpringsTest


class SpringsModel(object):
    @classmethod
    def save_springs_to_pickle_file(cls, file_path: str, springs_json_list: list):
        """
        :param file_path: full path to file
        :type file_path: str

        :param springs_json_list: list of springs to save
        :type springs_json_list: list[dict]

        :return: None
        """
        SpringDAO.insert_springs(
            file_path=file_path,
            springs=[Spring.parse(spring_json) for spring_json in springs_json_list]
        )

    @classmethod
    def load_springs_from_pickle_file(cls, file_path: str):
        """
        :param file_path: full path to file
        :type file_path: str

        :return: list of springs json version
        :rtype: list[dict]
        """
        return [spring.json() for spring in SpringDAO.get_springs(
            file_path=file_path
        )]

    @classmethod
    def generate_python_file_and_return_code(cls, file_path: str, springs_json_list: list):
        """
        :param file_path: full path to file
        :type file_path: str

        :param springs_json_list: list of springs to convert
        :type springs_json_list: list[dict]

        :return: generated file text
        :rtype: str
        """
        return SpringsToCodeParser.generate_python_file_from_springs_and_return_code(
            file_path=file_path,
            springs=[Spring.parse(spring_json) for spring_json in springs_json_list]
        )

    @classmethod
    def run_tests_and_return_results(cls, springs_json_list: list):
        """
        :param springs_json_list: list of springs to run test
        :type springs_json_list: list[dict]

        :return: test results message text
        :rtype: str
        """
        return SpringsTest.run_threads_and_collect_errors(
            springs=[Spring.parse(spring_json) for spring_json in springs_json_list]
        )
