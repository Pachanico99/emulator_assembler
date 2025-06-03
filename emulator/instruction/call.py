from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Call(Instruction):
    def __init__(self, label):
        self.label = label

    def execute(self, processor: Processor):
        next_index = processor.get_ip().get_index()
        processor.stack.append(next_index)
        processor.jump_ip(processor.runnable.lookup_table[self.label])

    @staticmethod
    def instruction_name() -> str:
        return "call"