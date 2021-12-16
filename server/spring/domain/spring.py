from server.spring.domain.operation import Operation, OPERATIONS_MAPPING


class Spring(object):
    def __init__(self, id, name, operations):
        """
        :param id: id of spring
        :type id: int

        :param name: thread name
        :type name: string

        :param operations: sequence of spring operations
        :type operations: list[Operation]
        """
        self.id = id
        self.name = name
        self.method_name = f"thread{self.id+1}"
        self.operations = operations

    @classmethod
    def parse(cls, spring_json):
        def _parse_operation(operation_json):
            operation = OPERATIONS_MAPPING.get(operation_json["id"])
            if not operation:
                raise AttributeError(f"OPERATION WITH {operation_json['id']} NOT EXIST")
            return operation.parse(operation_json)

        return Spring(
            id=spring_json["id"],
            name=spring_json["thread_name"],
            operations=[_parse_operation(oj) for oj in spring_json["operations"]]
        )

    def json(self):
        return {
            "id": self.id,
            "thread_name": self.name,
            "operations": [operation.json() for operation in self.operations]
        }

    def as_code(self):
        """
        :return: generated code of spring method
        :rtype: str
        """
        code = f"# Thread '{self.name}'\n" \
               f"def {self.method_name}():\n"
        tabs_q = 1
        tab = '\t'
        for operation in self.operations:
            code += tabs_q * tab + operation.code_row()
            if operation.id == Operation.ID_IF:
                tabs_q += 1
            elif operation.id == Operation.ID_ENDIF:
                tabs_q -= 1

            if tabs_q < 1:
                tabs_q += 1

        return code
