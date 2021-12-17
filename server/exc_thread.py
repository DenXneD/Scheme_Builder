from threading import Thread


class ExcThread(Thread):
    def __init__(self, name, target=None):
        Thread.__init__(self, target=target)
        self.name = name
        self.exception = None

    def status(self):
        status = f"{self.name}: "
        if self.exception:
            status += f"ERROR({self.exception})"
        else:
            status += "OK"
        return status + "\n"

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        except Exception as ex:
            self.exception = ex
        finally:
            del self._target, self._args, self._kwargs
