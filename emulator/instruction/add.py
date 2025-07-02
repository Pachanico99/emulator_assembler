from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Add(Instruction):
    def __init__(self, register, value):
        self.register = register
        self.value = None
        self.value_raw = value

    def execute(self, processor: Processor):
        self.value = self.get_value(self.value_raw, processor)

        sum = processor.get_register(self.register) + self.value
        processor.set_register(self.register, sum)
        processor.increment_ip()

    def get_value(self, value, processor: Processor) -> int:
        if isinstance(value, str):
            return processor.get_register(value)
        return int(value)

    @staticmethod
    def instruction_name() -> str:
        return "add"