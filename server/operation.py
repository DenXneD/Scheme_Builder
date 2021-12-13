from abc import abstractmethod
from erfa.helpers import classproperty


class Operation(object):
    _ID_IF = "if"
    _ID_ENDIF = "endif"
    _ID_ASSIGN = "assign"
    _ID_PRINT = "print"
    _ID_INPUT = "input"
    IDENTIFIERS = [_ID_IF, _ID_ENDIF, _ID_ASSIGN, _ID_PRINT, _ID_INPUT]

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
    id = Operation._ID_IF
    _SIGNS = ["==", "!=", ">", "<"]

    def __init__(self, var_name: str, sign: str, to_compare: str):
        assert sign in self._SIGNS
        self.var_name = var_name
        self.sign = sign
        self.to_compare = to_compare

    def parse(self, operation_json: dict):
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
        return f"if {self.var_name} {self.sign} {self.to_compare}:"


class EndConditionalOperation(Operation):
    id = Operation._ID_ENDIF

    def parse(self, operation_json: dict):
        return EndConditionalOperation()

    @classproperty
    def json(self):
        return {
            "id": self.id
        }

    @classproperty
    def code_row(self):
        return ""


class AssignmentOperation(Operation):
    id = Operation._ID_ASSIGN

    def __init__(self, var_name: str, to_assign: str):
        self.var_name = var_name
        self.to_assign = to_assign

    def parse(self, operation_json: dict):
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
        return f"{self.var_name} = {self.to_assign}"


class PrintOperation(Operation):
    id = Operation._ID_PRINT

    def __init__(self, var_name: str):
        self.var_name = var_name

    def parse(self, operation_json: dict):
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
        return f"print({self.var_name})"


class InputOperation(Operation):
    id = Operation._ID_INPUT

    def __init__(self, var_name: str):
        self.var_name = var_name

    def parse(self, operation_json: dict):
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
        return f"{self.var_name} = input()"


OPERATIONS = [AssignmentOperation, ConditionalOperation, EndConditionalOperation, InputOperation, PrintOperation]
OPERATIONS_MAPPING = {
    operation.id: operation for operation in OPERATIONS
}
