import re
from emulator.pointer.pointer import Pointer
from emulator.instruction.instruction_factory import InstructionFactory
from emulator.instruction.instruction import Instruction
from emulator.runnable import runnable
from emulator.runnable.runnable import Runnable

COMMENT_SYMBOLS = ['#',';']
MAIN_LABEL = 'main'

class Assembler:
    def __init__(self):
        self.lookup_table: dict[str, int] = {}                                 # Tabla de simbolos con formato {etiqueta: direccion}
        self.instructions: list[Instruction] = []                              # Lista de instrucciones parseadas
        self.sourceCodeInstructions: list[str] = []                            # Lista de instrucciones sin parsear
        self.errors: list[str] = []                                            # Lista de errores encontrados
        self.pointer = Pointer()                                               # Puntero
        self.main_label_index: int = -1                                        # Indice de la etiqueta de inicio

        # Defino los patrones de busqueda
        self.label_pattern = re.compile(r'^\s*[A-Za-z_][A-Za-z0-9_]*:\s*$')

        self.instruction_pattern = re.compile(r'^\s*(mov|add|inc|jmp|jnz|cmp|dec)\s+([A-Za-z0-9_]+(?:\s*,\s*[A-Za-z0-9_]+)?)\s*$')

        self.comment_start_pattern = re.compile(r'\s*[' + re.escape(''.join(COMMENT_SYMBOLS)) + r'].*$')

    def assemble(self, file_path: str) -> Runnable:
        try:
            with open(file_path, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    original_line = line.rstrip() # saco el '\n'

                    # Elimino los comentarios y espacios extra
                    line_without_comment = self.extractComment(original_line)
                    line_stripped = line_without_comment.strip()

                    # Ignoro las lineas vacias o que son solo comentarios
                    if not line_stripped:
                        continue

                    # Proceso la linea
                    try:
                        if self.isLabel(line_stripped):
                            label = line_stripped[:-1] # tomo todo menos los :
                            if label.lower() == MAIN_LABEL:
                                self.main_label_index = self.pointer.getIndex()
                                
                            if label in self.lookup_table:
                                # Si esta, entonces es una etiqueta duplicada y genero un Error
                                self.errors.append(f"[Línea {line_num}] Error: Etiqueta duplicada '{label}'")

                            self.lookup_table[label] = self.pointer.getIndex()
                            self.pointer.increment()
                            self.instructions.append(InstructionFactory.create_noop())

                        else:
                            self.sourceCodeInstructions.append(line_stripped)
                            instruction = self.parsear_instruccion(line_stripped)
                            self.instructions.append(instruction)
                            self.pointer.increment()

                    except Exception as e:
                        self.errors.append(f"[Línea {line_num}] Error: {str(e)}")

        except FileNotFoundError:
            self.errors.append(f"Archivo no encontrado '{file_path}'")
        except Exception as e:
            self.errors.append(f"Error al leer el archivo: {str(e)}")

        # Reviso que este la etiqueta main
        if self.main_label_index == -1:
            self.errors.append(f"Error: No se encontro la etiqueta '{MAIN_LABEL}' en el archivo.")

        # Reporto los errores
        if self.errors:
            print("Errores encontrados en el ensamblado:")
            for err in self.errors:
                print(err)
            print(f"Ensamblado fallido con {len(self.errors)} error/es.")
        #else:
            # log para debug
            """
            print("Archivo ensamblado correctamente.")
            print("\n--- Tabla de Símbolos ---")
            for label, address in self.lookup_table.items():
                print(f"{label}: {address}")
            print("\n--- Instrucciones Parseadas ---")
            for index, instr in enumerate(self.instructions):
                print("Name <" + instr.instruction_name() + ">" + ", Pos <" + str(index) + ">")
            """

        runnable = Runnable(self.main_label_index, self.instructions, self.sourceCodeInstructions, self.lookup_table)
        runnable.show_status()
        return runnable

    def extractComment(self, line: str) -> str:
        match = self.comment_start_pattern.search(line)
        if match:
            return line[:match.start()]
        return line


    def isOnlyComment(self, line: str) -> bool:
        line_leading_stripped = line.lstrip()
        if not line_leading_stripped:
            return False
        return line_leading_stripped[0] in COMMENT_SYMBOLS

    def isEmpty(self, line: str) -> bool:
        return not line or line.strip() == ""

    def isLabel(self, line: str) -> bool:
        return self.label_pattern.fullmatch(line) is not None

    def parsear_instruccion(self, line: str) -> Instruction:
        match = self.instruction_pattern.fullmatch(line)

        if match:
            name = match.group(1).lower()
            params = match.group(2)
            print(f"Nombre: {name}, Parámetros: {params}")

            # Los separo por coma y saco los espacios
            params = [p.strip() for p in params.split(',')]

            return InstructionFactory.create_instruction(name, params)
        else:
            raise Exception(f"Error: sintaxis incorrecta para instrucción: '{line}'")
