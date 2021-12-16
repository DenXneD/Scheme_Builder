import pickle
from server.spring.domain.spring import Spring


class SpringDAO(object):
    @classmethod
    def insert_springs(cls, file_path, springs):
        """
        :param file_path: full path to file
        :type file_path: str

        :param springs: spring objects list to save in pickle file
        :type springs: list[Spring]
        """

        with open(file_path, 'wb') as file:
            pickle.dump(springs, file)

    @classmethod
    def get_springs(cls, file_path):
        """
        :param file_path: full path to file
        :type file_path: str

        :return: springs list that was saved to pickle file
        :rtype: list[Spring]
        """

        with open(file_path, 'rb') as file:
            return pickle.load(file) or []
