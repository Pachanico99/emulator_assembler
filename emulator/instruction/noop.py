from emulator.processor.processor import Processor
from emulator.instruction.instruction import Instruction

class Noop(Instruction):
    def __init__(self):
        pass
        
    def execute(self, processor: Processor):
        processor.increment_ip()
        
    @staticmethod
    def instruction_name() -> str:
        return "noop"