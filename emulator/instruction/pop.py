from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Pop(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, processor: Processor):
        value = processor.stack.pop()
        processor.set_register(self.register, value)

    @staticmethod
    def instruction_name() -> str:
        return "pop"