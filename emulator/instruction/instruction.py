from abc import abstractmethod
from abc import ABCMeta

class Instruction(metaclass=ABCMeta):
    
    @abstractmethod
    def execute(self):
        pass