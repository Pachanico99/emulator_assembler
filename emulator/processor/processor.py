from emulator.pointer.pointer import Pointer

class Processor:
    def __init__(self, main_index:int):
        self.registers: dict[str, int] = {
            'ax': 0,
            'bx': 0,
            'cx': 0,
            'dx': 0
        }
        self.flag: bool = False
        self.ip = Pointer(main_index)

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

    def get_register(self, name: str):
        return self.registers.get(name)
    