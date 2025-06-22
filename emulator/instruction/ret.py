from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Ret(Instruction):
    def __init__(self):
        pass

    def execute(self, processor: Processor):
        next_index = processor.get_process().get_stack().pop()
        processor.jump_ip(next_index)

    @staticmethod
    def instruction_name() -> str:
        return "ret"