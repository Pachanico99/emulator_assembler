from emulator.instruction.mov import Mov
from emulator.instruction.add import Add
from emulator.instruction.inc import Inc
from emulator.instruction.jmp import Jmp
from emulator.instruction.jnz import Jnz
from emulator.instruction.cmp import Cmp
from emulator.instruction.dec import Dec
from emulator.instruction.noop import Noop
from emulator.instruction.instruction import Instruction

class InstructionFactory:
    @staticmethod
    def create_instruction(name, params) -> Instruction:
        if name == Mov.instruction_name():
            if len(params) != 2:
                raise Exception("MOV requiere 2 parametros.")
            return Mov(params[0], params[1])

        elif name == Add.instruction_name():
            if len(params) != 2:
                raise Exception("ADD requiere 2 parametros.")
            return Add(params[0], params[1])

        elif name == Inc.instruction_name():
            if len(params) != 1:
                raise Exception("INC requiere 1 parametro.")
            return Inc(params[0])
            
        elif name == Jmp.instruction_name():
            if len(params) != 1:
                raise Exception("JMP requiere 1 parametro.")
            return Jmp(params[0])

        elif name == Jnz.instruction_name():
            if len(params) != 1:
                raise Exception("JNZ requiere 1 parametro.")
            return Jnz(params[0])

        elif name == Cmp.instruction_name():
            if len(params) != 2:
                raise Exception("CMP requiere 2 parametros.")
            return Cmp(params[0], params[1])

        elif name == Dec.instruction_name():
            if len(params) != 1:
                raise Exception("DEC requiere 1 parametro.")
            return Dec(params[0])

        else:
            raise Exception(f"Instruccion desconocida: {name}")

    @staticmethod
    def create_noop() -> Instruction:
        return Noop()
