from .operation import Operation, OPERATIONS_MAPPING


class Spring(object):
    def __init__(self, id, operations):
        """
        :param id: id of spring
        :type id: string

        :param operations: sequence of spring operations
        :type operations: list[Operation]
        """
        self.id = id
        self.operations = operations

    def parse_operation(self, operation_json):
        operation = OPERATIONS_MAPPING.get(operation_json["id"])
        if not operation:
            raise AttributeError
        return operation.parse(operation_json)

    def parse(self, spring_json):
        return Spring(
            id=spring_json["id"],
            operations=[self.parse_operation(oj) for oj in spring_json["operations"]]
        )

    def json(self):
        return {
            "id": self.id,
            "operations": [operation.json for operation in self.operations]
        }
