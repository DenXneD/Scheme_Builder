from abc import abstractmethod
from erfa.helpers import classproperty


class Operation(object):
    ID_IF = "If"
    ID_ENDIF = "Endif"
    ID_ASSIGN = "Assign"
    ID_PRINT = "Print"
    ID_INPUT = "Input"
    ID_DUMMY = "dummy id"
    IDENTIFIERS = [ID_IF, ID_ENDIF, ID_ASSIGN, ID_PRINT, ID_INPUT]
    id = ID_DUMMY

    @abstractmethod
    def parse(self, operation_json: dict):
        """
        That method returns object of that class from his json version

        :param operation_json: json version of object
        :type operation_json: dict[str, Variable]

        :rtype: Operation
        """

    @abstractmethod
    def json(self):
        """
        That method returns json version of that object
        :rtype: dict
        """

    @abstractmethod
    def code_row(self):
        """
        This method returns row of python code from object data
        :rtype: str
        """


class ConditionalOperation(Operation):
    id = Operation.ID_IF
    _SIGNS = ["==", "!=", ">", "<"]

    def __init__(self, var_name: str, sign: str, to_compare: str):
        assert sign in self._SIGNS
        self.var_name = var_name
        self.sign = sign
        self.to_compare = to_compare

    @classmethod
    def parse(cls, operation_json: dict):
        return ConditionalOperation(
            var_name=operation_json["var_name"],
            sign=operation_json["sign"],
            to_compare=operation_json["to_compare"]
        )

    @classproperty
    def json(self):
        return {
            "id": self.id,
            "var_name": self.var_name,
            "sign": self.sign,
            "to_compare": self.to_compare
        }

    @classproperty
    def code_row(self):
        return f"if {self.var_name} {self.sign} {self.to_compare}:\n"


class EndConditionalOperation(Operation):
    id = Operation.ID_ENDIF

    @classmethod
    def parse(cls, operation_json: dict):
        return EndConditionalOperation()

    @classproperty
    def json(self):
        return {
            "id": self.id
        }

    @classproperty
    def code_row(self):
        return "\n"


class AssignmentOperation(Operation):
    id = Operation.ID_ASSIGN

    def __init__(self, var_name: str, to_assign: str):
        self.var_name = var_name
        self.to_assign = to_assign

    @classmethod
    def parse(cls, operation_json: dict):
        return AssignmentOperation(
            var_name=operation_json["var_name"],
            to_assign=operation_json["to_assign"],
        )

    @classproperty
    def json(self):
        return {
            "id": self.id,
            "var_name": self.var_name,
            "to_assign": self.to_assign
        }

    @classproperty
    def code_row(self):
        return f"{self.var_name} = {self.to_assign}\n"


class PrintOperation(Operation):
    id = Operation.ID_PRINT

    def __init__(self, var_name: str):
        self.var_name = var_name

    @classmethod
    def parse(cls, operation_json: dict):
        return PrintOperation(
            var_name=operation_json["var_name"]
        )

    @classproperty
    def json(self):
        return {
            "id": self.id,
            "var_name": self.var_name
        }

    @classproperty
    def code_row(self):
        return f"print({self.var_name})\n"


class InputOperation(Operation):
    id = Operation.ID_INPUT

    def __init__(self, var_name: str):
        self.var_name = var_name

    @classmethod
    def parse(cls, operation_json: dict):
        return InputOperation(
            var_name=operation_json["var_name"]
        )

    @classproperty
    def json(self):
        return {
            "id": self.id,
            "var_name": self.var_name
        }

    @classproperty
    def code_row(self):
        return f"{self.var_name} = input()\n"


OPERATIONS = [AssignmentOperation, ConditionalOperation, EndConditionalOperation, InputOperation, PrintOperation]
OPERATIONS_MAPPING = {
    operation.id: operation for operation in OPERATIONS
}
