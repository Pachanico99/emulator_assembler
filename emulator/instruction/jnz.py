from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Jnz(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor: Processor):
        if processor.get_flag():
            processor.jump_ip(processor.runnable.lookup_table[self.label])

    @staticmethod
    def instruction_name() -> str:
        return "jnz"