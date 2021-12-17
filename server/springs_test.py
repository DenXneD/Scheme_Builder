import os
from server.parser import SpringsToCodeParser


class SpringsTest(object):
    TEST_RUN_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\run_test.py"

    @classmethod
    def run_threads_and_collect_errors(cls, springs: list):
        """
        :type springs: list[server.spring.domain.spring.Spring]
        :return: test results message text
        """
        SpringsToCodeParser.generate_python_file_from_springs_and_return_code(
            file_path=cls.TEST_RUN_FILE_PATH,
            springs=springs
        )
        os.system(f'python {cls.TEST_RUN_FILE_PATH}')
        if not os.path.exists(SpringsToCodeParser.RESULT_FILE_PATH):
            results = "FATAL ERROR"
        else:
            with open(SpringsToCodeParser.RESULT_FILE_PATH, 'r') as file:
                results = file.read()
            os.remove(SpringsToCodeParser.RESULT_FILE_PATH)

        os.remove(cls.TEST_RUN_FILE_PATH)
        return results
