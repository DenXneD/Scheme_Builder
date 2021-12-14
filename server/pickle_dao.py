import pickle
from server.spring import Spring


class PickleDAO(object):
    @classmethod
    def insert_springs(cls, springs):
        """
        :param springs: spring objects list to save in pickle file
        :type springs: list[Spring]
        """

        with open('springs.pickle', 'wb') as file:
            pickle.dump(springs, file)

    @classmethod
    def get_springs(cls):
        """
        :return: springs list that was saved to pickle file
        :rtype: list[Spring]
        """

        with open('springs.pickle', 'rb') as file:
            return pickle.load(file) or []
