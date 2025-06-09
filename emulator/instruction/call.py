from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Call(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor: Processor):
        next_index = processor.get_ip().get_index()
        processor.get_process().get_stack().append(next_index + 1)
        processor.jump_ip(processor.get_process().get_runnable().get_lookup_table()[self.label])

    @staticmethod
    def instruction_name() -> str:
        return "call"