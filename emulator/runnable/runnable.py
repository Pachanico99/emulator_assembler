from emulator.context.context import Context
from emulator.pointer.pointer import Pointer

class Runnable:
    def __init__(self, main_index:int):
        self.pointer = Pointer(main_index)
        self.instructions = []
        self.context = Context()
        
    def run(self):
        pass