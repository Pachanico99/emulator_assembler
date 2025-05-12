from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Dec(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, processor: Processor):
        current_value = processor.get_register(self.register)
        decrement = current_value - 1
        processor.set_register(self.register, decrement)

    def set_values(self, register, processor: Processor):
        if isinstance(register, str):
            self.register = processor.get_register(register)
            
    @staticmethod
    def instruction_name() -> str:
        return "dec"
