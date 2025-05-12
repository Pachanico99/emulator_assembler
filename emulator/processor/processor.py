from emulator.pointer.pointer import Pointer
from emulator.runnable.runnable import Runnable

class Processor:
    def __init__(self, main_index:int, runnable: Runnable):
        self.registers: dict[str, int] = {
            'ax': 0,
            'bx': 0,
            'cx': 0,
            'dx': 0
        }
        self.flag: bool = False
        self.ip = Pointer(main_index)
        self.runnable = runnable

    def get_registers(self):
        return self.registers
    
    def set_flag_false(self):
        self.flag = False

    def set_flag_true(self):
        self.flag = True

    def get_flag(self):
        return self.flag

    def increment_ip(self):
        self.ip.increment()

    def jump_ip(self, index: int):
        self.ip.set_index(index)

    def get_ip(self):
        return self.ip

    def get_register(self, name: str) -> int:
        return self.registers.get(name)

    def set_register(self, name: str, value: int):
        self.registers[name] = value

    def step(self):
        if self.ip.get_index() < len(self.runnable.instructions):
            instruction = self.runnable.instructions[self.ip.get_index()]
            instruction.execute(self)
            self.ip.increment()
    