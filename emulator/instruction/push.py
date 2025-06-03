from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Push(Instruction):
    def __init__(self, value):
        self.value = value

    def execute(self, processor: Processor):
        processor.stack.append(self.get_value(self.value, processor))

    def get_value(self, value, processor: Processor):
        if isinstance(value, str):
            return processor.get_register(value)
        return value

    @staticmethod
    def instruction_name() -> str:
        return "push"