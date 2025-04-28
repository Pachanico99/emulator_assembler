from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Cmp(Instruction):
    def __init__(self, register, value):
        self.register = register
        self.value = value
        
    def execute(self, processor:Processor):
        pass

    @staticmethod
    def instruction_name() -> str:
        return "cmp"