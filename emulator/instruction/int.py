from emulator.processor.processor import Processor
from emulator.instruction.instruction import Instruction

class Int(Instruction):
    def __init__(self, system_call_number):
        self.system_call_number = system_call_number

    def execute(self, processor: Processor):
        operating_system = processor.get_operating_system()
        if self.system_call_number == 1:
            parametros = [
                processor.get_register("ax"),  # valor literal
                processor.get_register("bx"),  # fila
                processor.get_register("cx")   # columna
            ]
            operating_system.system_call_handler(self.system_call_number, parametros)
        else:
            raise RuntimeError("Syscall no implementada: %d" % self.system_call_number)
        processor.increment_ip()

    @staticmethod
    def instruction_name() -> str:
        return "int"