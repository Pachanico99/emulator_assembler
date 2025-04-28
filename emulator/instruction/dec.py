from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Dec(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, processor:Processor):
        pass

    @staticmethod
    def instruction_name() -> str:
        return "dec"
