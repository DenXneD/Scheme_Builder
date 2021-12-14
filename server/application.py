from server.spring.domain.spring import Spring
from server.spring.pickle_dao import SpringDAO
from server.parser import SpringsToCodeParser


class SpringsModel(object):
    @classmethod
    def save_springs_to_pickle_file(cls, springs_json_list: list):
        """
        :param springs_json_list: list of springs to save
        :type springs_json_list: list[dict]
        """
        SpringDAO.insert_springs(
            springs=[Spring.parse(spring_json) for spring_json in springs_json_list]
        )

    @classmethod
    def load_springs_from_pickle_file(cls):
        """
        :return: list of springs json version
        :rtype: list[dict]
        """
        return [spring.json for spring in SpringDAO.get_springs()]

    @classmethod
    def generate_springs_python_file(cls, springs_json_list: list):
        """
        :param springs_json_list: list of springs to convert
        :type springs_json_list: list[dict]

        :return: generated file text
        :rtype: str
        """
        return SpringsToCodeParser.parse_springs_to_code(
            springs=[Spring.parse(spring_json) for spring_json in springs_json_list]
        )