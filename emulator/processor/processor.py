from emulator.process.process import Process
from emulator.emulator_gui.emulator_gui import EmulatorCLI
from enum import Enum
from emulator.pointer.pointer import Pointer
import time
from emulator.config.config import Config

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from emulator.operating_system.operating_system import OperatingSystem



class ProcessorStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Processor:
    def __init__(self, process: Process=None, emulator_cli: EmulatorCLI=None, operating_system: "OperatingSystem"=None):
        self.registers: dict[str, int] = {
            'ax': 0,
            'bx': 0,
            'cx': 0,
            'dx': 0
        }
        self.flag: bool = False
        self.ip: Pointer = None
        self.current_process: Process = process
        self.emulator_cli: EmulatorCLI = emulator_cli
        self.operating_system: "OperatingSystem" = operating_system
        self.status: ProcessorStatus = ProcessorStatus.INACTIVE
        self.video_memory: list[list[int]] = [[0 for _ in range(Config.get_video_memory_width())] for _ in range(Config.get_video_memory_height())]

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

    def get_process(self):
        return self.current_process

    def get_status(self):
        return self.status

    def set_status(self, status: ProcessorStatus):
        self.status = status

    def get_operating_system(self):
        return self.operating_system

    def set_operating_system(self, operating_system: "OperatingSystem"):
        self.operating_system = operating_system
        self.status = ProcessorStatus.ACTIVE

    def set_process(self, process: Process):
        self.registers = process.get_context().get_registers().copy()
        self.flag = process.get_context().get_flag()
        self.ip = Pointer(process.get_context().get_ip().get_index())
        self.current_process = process
        self.video_memory = process.get_context().get_video_memory().copy()

    def set_first_process(self, current_process: Process):
        self.current_process = current_process
        self.ip = Pointer(current_process.get_runnable().get_main_index())

    def get_video_memory(self):
        return self.video_memory

    def set_video_memory(self, video_memory: list[list[int]]):
        self.video_memory = video_memory

    def process(self):
        self.emulator_cli.draw_view(self)
        time.sleep(Config.get_auto_run_interval_seconds())

        while self.get_status() == ProcessorStatus.ACTIVE:
            instruction = self.current_process.get_runnable().get_instructions()[self.ip.get_index()]
            instruction.execute(self)

            self.emulator_cli.draw_view(self)
            time.sleep(Config.get_auto_run_interval_seconds())

            self.operating_system.clock_handler()

            
            