from __future__ import annotations

class Runnable:
    def __init__(self, main_index:int, instructions: list["Instruction"], sourceCodeInstructions: list[str], lookup_table: dict[str, int], file_name: str):
        self.instructions =  instructions
        self.sourceCodeInstructions = sourceCodeInstructions
        self.lookup_table = lookup_table
        self.main_index = main_index
        self.file_name = file_name

    def get_instructions(self):
        return self.instructions

    def get_sourceCodeInstructions(self):
        return self.sourceCodeInstructions

    def get_lookup_table(self):
        return self.lookup_table

    def get_main_index(self):
        return self.main_index

    def get_file_name(self):
        return self.file_name

    def show_status(self):
        print(f'\n----- ---- ---- -----')
        print(f'-----   STATUS  -----')
        print(f'----- ---- ---- -----')

        print(f'\n--- File Name ---')
        print(f'File Name: {self.file_name}')

        print(f'\n--- Main Index ---')
        print(f'Index: {self.main_index}')

        print("\n--- Tabla de Etiquetas ---")
        for label, address in self.lookup_table.items():
            print(f"Etiqueta: {label}, Indice: {address}")

        print("\n--- Instrucciones Parseadas ---")
        for index, instr in enumerate(self.instructions):
            print("Nombre: <" + instr.instruction_name() + ">" + "\nPos: <" + str(index) + ">")

        print("\n--- Instrucciones sin Parsear ---")
        for index, instr in enumerate(self.sourceCodeInstructions):
            print("Instruccion: <" + instr + ">" + "\nPos: <" + str(index) + ">")

