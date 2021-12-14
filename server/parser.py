class SpringsToCodeParser(object):
    @classmethod
    def parse_springs_to_code(cls, springs):
        """
        :param springs: springs to parse list
        :type springs: list[server.spring.Spring]

        :return: generated code
        :rtype: str
        """
        code = ""
        for spring in springs:
            code += spring.as_code() + "\n\n"

        for spring in springs:
            code += f"{spring.name}()\n"

        with open('../generated.py', 'w+') as file:
            file.write(code)

        return code
