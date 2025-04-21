from emulator.pointer.pointer import Pointer

#ver si conviene usar esta clase o definir todo dentro de assembler y runnable

class Context:
    def __init__(self):
        # consultar por el tema de los registros, si son predefinidos o se pueden definir
        self.registers = {
            'ax': 0,
            'bx': 0,
            'cx': 0,
            'dx': 0
        }
        self.lookup_table = {}
        # ver donde colocar el ip
        
    def add_register(self, name:str, value:object):
        self.registers[name] = value

    def addLabel(self, name:str, value:int):
        self.lookup_table[name] = value

    def getRegisterValue(self, name:str) -> object:
        return self.registers[name]

    def getLabelIndex(self, name:str) -> int:
        return self.lookup_table[name]
