from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Cmp(Instruction):
    def __init__(self, raw_value1, raw_value2):
        self.raw_value1 = raw_value1
        self.raw_value2 = raw_value2
        self.value1: int = None
        self.value2: int = None
        
    def execute(self, processor: Processor):
        self.set_values(processor)

        processor.set_flag_eq(self.value1 == self.value2)
        processor.set_flag(self.value1 < self.value2)

        processor.increment_ip()

    def set_values(self, processor: Processor):
        self.value1 = processor.get_register(self.raw_value1) if isinstance(self.raw_value1, str) else self.raw_value1
        self.value2 = processor.get_register(self.raw_value2) if isinstance(self.raw_value2, str) else self.raw_value2

    @staticmethod
    def instruction_name() -> str:
        return "cmp"
