from .operation import Operation, OPERATIONS_MAPPING


class Spring(object):
    def __init__(self, id, operations):
        """
        :param id: id of spring
        :type id: int

        :param operations: sequence of spring operations
        :type operations: list[Operation]
        """
        self.id = id
        self.operations = operations

    def parse(self, spring_json):
        def _parse_operation(operation_json):
            operation = OPERATIONS_MAPPING.get(operation_json["id"])
            if not operation:
                raise AttributeError
            return operation.parse(operation_json)

        return Spring(
            id=spring_json["id"],
            operations=[_parse_operation(oj) for oj in spring_json["operations"]]
        )

    def json(self):
        return {
            "id": self.id,
            "operations": [operation.json for operation in self.operations]
        }

    def as_code(self):
        """
        :raises BrokenPipeError: when user put incorrect conditional operations sequence
        """
        code = f"def spring{self.id}():\n"
        tabs_q = 1
        tab = '\t'
        for operation in self.operations:
            code += tabs_q * tab + operation.code_row()
            if operation.id == Operation.ID_IF:
                tabs_q += 1
            elif operation.id == Operation.ID_ENDIF:
                tabs_q -= 1

            if tabs_q < 1:
                raise BrokenPipeError



