from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Jl(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor: Processor):
        if processor.get_flag():
            processor.jump_ip(processor.get_process().get_runnable().get_lookup_table()[self.label])
        else:
            processor.increment_ip()

    @staticmethod
    def instruction_name() -> str:
        return "jl"
