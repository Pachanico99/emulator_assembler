from emulator.instruction.mov import Mov
from emulator.instruction.add import Add
from emulator.instruction.inc import Inc
from emulator.instruction.jmp import Jmp
from emulator.instruction.jnz import Jnz
from emulator.instruction.cmp import Cmp

class InstructionFactory:
    @staticmethod
    def create_instruction(nombre, parametros):
        if nombre == "mov":
            if len(parametros) != 2:
                raise Exception("MOV requiere 2 parámetros.")
            return Mov(parametros[0], parametros[1])
        elif nombre == "add":
            if len(parametros) != 2:
                raise Exception("ADD requiere 2 parámetros.")
            return Add(parametros[0], parametros[1])
        elif nombre == "inc":
            if len(parametros) != 1:
                raise Exception("INC requiere 1 parámetro.")
            return Inc(parametros[0])
        elif nombre == "jmp":
            if len(parametros) != 1:
                raise Exception("JMP requiere 1 parámetro.")
            return Jmp(parametros[0])
        elif nombre == "jnz":
            if len(parametros) != 1:
                raise Exception("JNZ requiere 1 parámetro.")
            return Jnz(parametros[0])
        elif nombre == "cmp":
            if len(parametros) != 2:
                raise Exception("CMP requiere 2 parámetros.")
            return Cmp(parametros[0], parametros[1])
        else:
            raise Exception(f"Instrucción desconocida: {nombre}")
