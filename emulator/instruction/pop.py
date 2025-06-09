from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Pop(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, processor: Processor):
        value = processor.get_process().get_stack().pop()
        processor.set_register(self.register, value)
        processor.increment_ip()

    @staticmethod
    def instruction_name() -> str:
        return "pop"