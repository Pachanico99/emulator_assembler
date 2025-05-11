from emulator.instruction.instruction import Instruction

class Runnable:
    def __init__(self, main_index:int, instructions: list[Instruction], sourceCodeInstructions: list[str], lookup_table: dict[str, int]):
        self.instructions =  instructions
        self.sourceCodeInstructions = sourceCodeInstructions
        self.lookup_table = lookup_table
        self.main_index = main_index
        
    def run(self):
        pass

    def show_status(self):
        print(f'\n----- ---- ---- -----')
        print(f'-----   STATUS  -----')
        print(f'----- ---- ---- -----')
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

