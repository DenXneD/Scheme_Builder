class SpringsToCodeParser(object):
    @classmethod
    def parse_springs_to_code(cls, springs):
        """
        :param springs: springs to parse list
        :type springs: list[server.spring.domain.spring.Spring]

        :return: generated code
        :rtype: str
        """
        code = ""
        for spring in springs:
            code += spring.as_code() + "\n"

        for spring in springs:
            code += f"{spring.method_name}()\n"

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
