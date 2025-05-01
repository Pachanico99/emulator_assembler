from emulator.processor.processor import Processor
from emulator.pointer.pointer import Pointer
from emulator.instruction.instruction import Instruction

class Runnable:
    def __init__(self, main_index:int, instructions: list[Instruction], source_code_instructions: list[str], lookup_table: dict[str, int]):
        self.pointer = Pointer(main_index)
        self.instructions =  instructions
        self.source_code_instructions = source_code_instructions
        self.lookup_table = lookup_table

    def show_status(self):
        print(f'\n----- ---- ---- -----')
        print(f'-----   STATUS  -----')
        print(f'----- ---- ---- -----')
        print(f'\n--- Pointer ---')
        print(f'Index: {self.pointer.get_index()}')

        print("\n--- Tabla de Etiquetas ---")
        for label, address in self.lookup_table.items():
            print(f"Etiqueta: {label}, Indice: {address}")

        print("\n--- Instrucciones Parseadas ---")
        for index, instr in enumerate(self.instructions):
            print("Nombre: <" + instr.instruction_name() + ">" + "\nPos: <" + str(index) + ">")

        print("\n--- Instrucciones sin Parsear ---")
        for index, instr in enumerate(self.source_code_instructions):
            print(instr + "    -----    Pos: <" + str(index) + ">")

