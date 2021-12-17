import string


class ErrorTest:
    def __init__(self, data_to_check):
        self.data_to_check = data_to_check

    def is_number(self):
        try:
            int(self.data_to_check)
            return True
        except:
            return False

    def variable_is_acceptable(self):
        acceptable_chars = string.ascii_letters + string.digits
        for letter_index in range(len(self.data_to_check)):
            if self.data_to_check[letter_index] not in acceptable_chars or \
                    (self.data_to_check[letter_index] in string.digits and letter_index == 0):
                return False
        return True

    def print_is_acceptable(self):
        acceptable_chars = string.ascii_letters + string.digits
        for letter_index in range(len(self.data_to_check)):
            if self.data_to_check[letter_index] not in acceptable_chars:
                return False
        return True
