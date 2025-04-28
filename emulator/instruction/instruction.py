from abc import abstractmethod
from abc import ABCMeta
from emulator.processor.processor import Processor

class Instruction(metaclass=ABCMeta):
    
    @abstractmethod
    def execute(self, processor:Processor):
        pass

    @staticmethod
    @abstractmethod
    def instruction_name():
        pass