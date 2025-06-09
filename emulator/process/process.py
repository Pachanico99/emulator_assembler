from emulator.runnable.runnable import Runnable
from emulator.process.context import Context
from enum import Enum

class ProcessStatus(Enum):
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    FINISHED = "FINISHED"

class Process:
    def __init__(self, runnable: Runnable=None, stack: list[int]=None, status: ProcessStatus=ProcessStatus.BLOCKED):
        self.context: Context = Context(runnable.get_main_index())
        self.stack: list[int] = stack if stack is not None else []
        self.runnable: Runnable = runnable
        self.status: ProcessStatus = status

    def get_context(self):
        return self.context

    def get_runnable(self):
        return self.runnable

    def get_stack(self):
        return self.stack

    def get_status(self):
        return self.status

    def set_status(self, status: ProcessStatus):
        self.status = status

    def set_context(self, context: Context):
        self.context = context