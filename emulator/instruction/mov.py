from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Mov(Instruction):
    def __init__(self, register, raw_value):
        self.register = register
        self.raw_value = raw_value
        self.value: int = None

    def execute(self, processor: Processor):
        self.set_value(processor)
        processor.set_register(self.register, self.value)
        processor.increment_ip()

    def set_value(self, processor: Processor):
        if isinstance(self.raw_value, str):
            self.value = processor.get_register(self.raw_value)
        else:
            self.value = int(self.raw_value)
        
    @staticmethod
    def instruction_name() -> str:
        return "mov"