from emulator.pointer.pointer import Pointer

class Processor:
    def __init__(self):
        self.registers: dict[str, int] = {
            'ax': 0,
            'bx': 0,
            'cx': 0,
            'dx': 0
        }
        self.flag: bool = False
        self.ip = Pointer(0)
    
    def set_flag_false(self):
        self.flag = False

    def set_flag_true(self):
        self.flag = True

    def increment_ip(self):
        self.ip.increment()

    def getRegisters(self):
        return self.registers

    def getFlag(self):
        return self.flag

    def getIp(self):
        return self.ip
