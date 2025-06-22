from emulator.pointer.pointer import Pointer
from emulator.config.config import Config

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
        self.video_memory: list[list[int]] = [[0 for _ in range(Config.get_video_memory_width())] for _ in range(Config.get_video_memory_height())]
    
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

    def get_video_memory(self):
        return self.video_memory

    def set_video_memory(self, video_memory: list[list[int]]):
        self.video_memory = video_memory