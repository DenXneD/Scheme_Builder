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
            code += spring.as_code() + "\n\n"

        for spring in springs:
            code += f"{spring.name}()\n"

        return code

    @classmethod
    def generate_python_file_from_springs(cls, springs):
        """
        :param springs: springs to generate python code
        :type springs: list[server.spring.domain.spring.Spring]

        :return: generated code
        :rtype: str
        """
        code = cls.parse_springs_to_code(springs)
        with open('../generated.py', 'w+') as file:
            file.write(code)

        return code
