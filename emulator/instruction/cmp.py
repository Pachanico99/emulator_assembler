from emulator.instruction.instruction import Instruction
from emulator.processor.processor import Processor

class Cmp(Instruction):
    def __init__(self, register, value):
        self.register_name = register
        self.value_raw = value
        self.register_value = None
        self.value = None
        
    def execute(self, processor: Processor):
        self.set_values(processor)
        
        if self.register_value == self.value:
            processor.set_flag_false()
        else:
            processor.set_flag_true()

    def set_values(self, processor: Processor):
        if isinstance(self.value_raw, str):
            self.value = processor.get_register(self.value_raw)
        else:
            self.value = self.value_raw

        self.register_value = processor.get_register(self.register_name)

    @staticmethod
    def instruction_name() -> str:
        return "cmp"

