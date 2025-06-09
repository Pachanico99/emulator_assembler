from emulator.pointer.pointer import Pointer

class Context:
    def __init__(self, main_index: int=None):
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

    def set_registers(self, registers: dict[str, int]):
        self.registers = registers

    def set_register_by_name(self, register: str, value: int):
        self.registers[register] = value

    def get_flag(self):
        return self.flag

    def set_flag(self, flag: bool):
        self.flag = flag

    def get_ip(self):
        return self.ip

    def set_ip(self, ip: Pointer):
        self.ip = ip 