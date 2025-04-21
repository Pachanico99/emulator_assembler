from emulator.pointer.pointer import Pointer
from emulator.instruction.instruction_factory import InstructionFactory
from emulator.instruction.instruction import Instruction
import re

COMMENT_SYMBOLS = [';']

class Assembler:
    def __init__(self):
        self.lookup_table = {}  # Etiquetas -> posiciones
        self.instructions = []  # Lista de instrucciones (instancias)
        self.errors = []
        self.pointer = Pointer(0)

        # ver donde colocar
        #for symbol in COMMENT_SYMBOLS:
        #    line = line.split(symbol)[0]

    def assemble(self, file):
        with open(file, 'r') as file:
            for line in file:
                # ignorar las lines vacias o comentadas
                if self.isEmpty(line) or self.isOnlyComment(line):
                    continue
                else:
                    line = self.extractComment(line)

                try:
                    if self.isLabel(line):
                        label = line[:-1] # tomo todo menos los :
                        if label in self.lookup_table:
                            raise Exception(f"Etiqueta duplicada: {label}")
                        self.lookup_table[label] = None # ver que posicion
                    else:
                        instruccion = self._parsear_instruccion(line)
                        self.instructions.append(instruccion)
                except Exception as e:
                    self.errors.append(f"[Línea {self.pointer.getIndex()}] Error: {str(e)}")

        if self.errors:
            for err in self.errors:
                print(err)
        else:
            print("Archivo ensamblado correctamente.")
            print("Archivo ensamblado correctamente.")

    def extractComment(self, line:str) -> str:
        # implementar 
        return line

    def isOnlyComment(self, line:str) -> bool:
        for symbol in line:
            if line.startswith(symbol):
                return True
        return False

    def isEmpty(self, line:str) -> bool:
        return not line

    def isLabel(self, line:str) -> str:
        # formato de nombre de la etiqueta, seguido por ':' al final
        pattern = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*:$')
        return pattern.fullmatch(line) is not None

    def _parsear_instruccion(self, line) -> 'Instruction':
        pattern = re.compile(r'^\s*(mov|add|inc|jmp|jnz|cmp|dec)\s+([A-Za-z0-9]+(?:\s*,\s[A-Za-z0-9]+)?)\s*$')
        match = pattern.match(line)

        if match:
            name = match.group(1).lower() 
            params = match.group(2).split(',')
            params = [p.strip() for p in params] # saco los espacios

            return InstructionFactory.create_instruction(name, params)
        else:
            raise Exception(f"Formato incorrecto para la instrucción: {line}")
