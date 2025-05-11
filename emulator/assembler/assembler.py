import re
from emulator.pointer.pointer import Pointer
from emulator.instruction.instruction_factory import InstructionFactory
from emulator.instruction.instruction import Instruction
from emulator.instruction.jnz import Jnz
from emulator.instruction.jmp import Jmp
from emulator.runnable.runnable import Runnable
from emulator.config.config import Config

class Assembler:
    def __init__(self):
        self.lookup_table: dict[str, int] = {}                                 # Tabla de simbolos {etiqueta: direccion}
        self.instructions: list[Instruction] = []                              # Lista de instrucciones parseadas
        self.sourceCodeInstructions: list[str] = []                            # Lista de instrucciones sin parsear
        self.errors: list[str] = []                                            # Lista de errores encontrados
        self.pointer = Pointer()                                               # Puntero
        self.main_label_index: int = -1                                        # Indice de la etiqueta de inicio
        self.lookup_table_validation: list[tuple[str, int]] = []               # Tabla de simbolos para validar {etiqueta: existencia}

        # Defino los patrones de busqueda
        self.label_pattern = re.compile(r'^\s*[A-Za-z_][A-Za-z0-9_]*:\s*$')

        self.instruction_pattern = re.compile(r'^\s*(' + Config.get_valid_instruction_pattern() + r')(?:\s+(.*))?\s*$')

        self.comment_start_pattern = re.compile(r'\s*[' + Config.get_comment_symbols_pattern() + r'].*$')

    def assemble(self, file_path: str) -> Runnable:
        try:
            with open(file_path, 'r') as file:
                print(f"Ensamblando archivo: {file.name}")

                for line_num, line in enumerate(file, 1):
                    #print(f"Línea {line_num}: {line}")                                                                 # debug

                    # Elimino los comentarios y espacios extra
                    original_line = line.rstrip()
                    line_without_comment = self.extractComment(original_line)
                    line_stripped = line_without_comment.strip()

                    #print(f"Línea {line_num}: {line_stripped}")                                                        # debug

                    # Ignoro las lineas vacias o que son solo comentarios
                    if not line_stripped:
                        continue

                    try:
                        if self.isLabel(line_stripped):
                            label = line_stripped[:-1].lower() # tomo todo menos los :
                            if label == Config.get_label_main_name():
                                self.main_label_index = self.pointer.get_index()
                                
                            if label in self.lookup_table:
                                # Si esta, entonces es una etiqueta duplicada y genero un error
                                self.errors.append(f"[Línea {line_num}] Error: Etiqueta duplicada '{label}'")

                            self.lookup_table[label] = self.pointer.get_index()
                            self.instructions.append(InstructionFactory.create_noop())

                        else:
                            instruction = self.parsear_instruccion(line_stripped, line_num)
                            self.instructions.append(instruction)

                        self.pointer.increment()
                        self.sourceCodeInstructions.append(line_stripped)
                    except Exception as e:
                        self.errors.append(f"[Línea {line_num}] Error: {str(e)}")
                
        except FileNotFoundError:
            self.errors.append(f"Archivo no encontrado '{file_path}'")
        except Exception as e:
            self.errors.append(f"Error al leer el archivo: {str(e)}")

        # Reviso que este la etiqueta main
        if self.main_label_index == -1:
            self.errors.append(f"Error: No se encontro la etiqueta '{Config.get_label_main_name()}' en el archivo.")

        # Reviso que las etiquetas que se usaron en las instrucciones existan
        for label, index in self.lookup_table_validation:
            if label not in self.lookup_table:
                self.errors.append(f"[Línea {index}] Error: Etiqueta '{label}' no encontrada en el archivo.")

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
            print("\n--- Tabla de Etiquetas ---")
            for label, address in self.lookup_table.items():
                print(f"{label}: {address}")
            print("\n--- Instrucciones Parseadas ---")
            for index, instr in enumerate(self.instructions):
                print("Name <" + instr.instruction_name() + ">" + ", Pos <" + str(index) + ">")
            """

        runnable = Runnable(self.main_label_index, self.instructions, self.sourceCodeInstructions, self.lookup_table)
        #runnable.show_status()
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
        return line_leading_stripped[0] in Config.get_comment_symbols()

    def isEmpty(self, line: str) -> bool:
        return not line or line.strip() == ""

    def isLabel(self, line: str) -> bool:
        return self.label_pattern.fullmatch(line) is not None

    def parsear_instruccion(self, line: str, index: int) -> Instruction:
        match = self.instruction_pattern.fullmatch(line)
        #print(match)                                                                                                   # debug                   

        if match:
            name = match.group(1).lower()
            params = match.group(2)

            #print(f"Nombre: {name}, Parámetros: {params}")                                                             # debug

            # Los separo por coma y saco los espacios
            if params is not None:
                raw_params = [p.strip() for p in params.lower().split(',')]
            else:
                raw_params = []

            instruction = InstructionFactory.create_instruction(name, raw_params)

            if isinstance(instruction, Jnz) or isinstance(instruction, Jmp):
                #print(f"Etiqueta: {raw_params[0]}, Indice: {index}")                                                   # debug          
                self.lookup_table_validation.append((raw_params[0], index))

            return instruction
        else:
            raise Exception(f"Instruccion invalida: '{line}'")
