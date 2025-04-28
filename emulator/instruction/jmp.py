from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Jmp(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor:Processor):
        pass

    @staticmethod
    def instruction_name() -> str:
        return "jmp"