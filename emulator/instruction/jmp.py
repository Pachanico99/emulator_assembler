from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Jmp(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor: Processor):
        processor.jump_ip(processor.get_process().get_runnable().get_lookup_table()[self.label])

    @staticmethod
    def instruction_name() -> str:
        return "jmp"