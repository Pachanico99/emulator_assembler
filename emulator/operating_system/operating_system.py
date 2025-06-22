from emulator.process.process import Process
from emulator.config.config import Config
from emulator.process.process import ProcessStatus
from emulator.processor.processor import ProcessorStatus
from emulator.process.context import Context
from emulator.pointer.pointer import Pointer

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from emulator.processor.processor import Processor

class OperatingSystem:
    def __init__(self, processes: list[Process]=[], processor: "Processor"=None ,quantity_of_instructions_per_burst: int=0):
        self.processes: list[Process] = processes
        self.quantity_of_instructions_per_burst = quantity_of_instructions_per_burst
        self.processor: "Processor" = processor
        self.index_last_process_processed: int = 0
    
    def clock_handler(self):
        self.quantity_of_instructions_per_burst += 1
        finish_process = self.processor.get_ip().get_index() >= len(self.processor.get_process().get_runnable().get_instructions())

        if self.quantity_of_instructions_per_burst >= Config.get_quantity_of_instructions_per_burst() or finish_process:
            if finish_process:
                self.processor.get_process().set_status(ProcessStatus.FINISHED)
            else:
                context = Context()
                context.set_registers(self.processor.get_registers().copy())
                context.set_flag(self.processor.get_flag())
                context.set_ip(Pointer(self.processor.get_ip().get_index()))
                context.set_video_memory(self.processor.get_video_memory().copy())
                self.processor.get_process().set_context(context)
                self.processor.get_process().set_status(ProcessStatus.BLOCKED)
            
            process = self._find_next_process()
            
            if process:
                self.processor.set_process(process)
                self.quantity_of_instructions_per_burst = 0
            else:
                self.processor.set_status(ProcessorStatus.INACTIVE)
    
    def _find_next_process(self) -> "Process":
        total_processes = len(self.processes)
        attempts = 0

        while attempts < total_processes:
            self.index_last_process_processed = (self.index_last_process_processed + 1) % total_processes
            process = self.processes[self.index_last_process_processed]

            if process.get_status() == ProcessStatus.BLOCKED:
                return process

            attempts += 1

        return None

    def system_call_handler(self, system_call_number, parameters):
        if system_call_number == 1:
            value, row, column = parameters
            if row < 0 or row >= Config.get_video_memory_height():
                raise RuntimeError("Fila fuera de rango")
            if column < 0 or column >= Config.get_video_memory_width():
                raise RuntimeError("Columna fuera de rango")
            self.processor.get_video_memory()[row][column] = value
        else:
            raise RuntimeError("Servicio SO desconocido: %d" % system_call_number)