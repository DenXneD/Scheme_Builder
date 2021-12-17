import os


class SpringsToCodeParser(object):
    RESULT_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\mem_result_data.txt"

    @classmethod
    def parse_springs_to_code(cls, springs):
        """
        :param springs: springs to parse list
        :type springs: list[server.spring.domain.spring.Spring]

        :return: generated code
        :rtype: str
        """
        code = "from server.exc_thread import ExcThread\nfrom server.parser import SpringsToCodeParser\n\n"

        for spring in springs:
            code += spring.as_code() + "\n\n"

        code += "results = ''\n"
        code += "threads = []\n"
        for spring in springs:
            code += f"thread = ExcThread(name='{spring.id + 1}. {spring.name}', target={spring.method_name})\n" \
                    f"threads.append(thread)\n" \
                    f"thread.start()\n" \


        code += f"[thread.join() for thread in threads]\n\n\n"
        code += f"for thread in threads:\n" \
                f"    results += thread.status()\n"

        code += f"""with open(SpringsToCodeParser.RESULT_FILE_PATH, "w+") as file:\n""" \
                f"    file.write(results)"

        return code

    @classmethod
    def generate_python_file_from_springs_and_return_code(cls, file_path, springs):
        """
        :param file_path: full path to file
        :type file_path: str

        :param springs: springs to generate python code
        :type springs: list[server.spring.domain.spring.Spring]

        :return: generated code
        :rtype: str
        """
        code = cls.parse_springs_to_code(springs)
        with open(file_path, 'w+') as file:
            file.write(code)

        return code
