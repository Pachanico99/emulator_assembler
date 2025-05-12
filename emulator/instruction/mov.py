from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Mov(Instruction):
    def __init__(self, register, value):
        self.register = register
        self.value = value

    def execute(self, processor: Processor):
        self.set_value(self.value, processor)
        processor.set_register(self.register, self.value)

    def set_value(self, value, processor: Processor):
        if isinstance(value, str):
            self.value = processor.get_register(value)
        
    @staticmethod
    def instruction_name() -> str:
        return "mov"