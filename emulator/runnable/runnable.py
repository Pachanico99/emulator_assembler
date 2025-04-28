from emulator.processor.processor import Processor
from emulator.pointer.pointer import Pointer
from emulator.instruction.instruction import Instruction

class Runnable:
    def __init__(self, main_index:int, instructions: list[Instruction], sourceCodeInstructions: list[str], lookup_table: dict[str, int]):
        self.pointer = Pointer(main_index)
        self.instructions =  instructions
        self.sourceCodeInstructions = sourceCodeInstructions
        self.lookup_table = lookup_table
        self.ip = Pointer(main_index)
        self.processor = Processor()
        
    def run(self):
        pass

    def show_status(self):
        print(f'\n----- ---- ---- -----')
        print(f'-----   STATUS  -----')
        print(f'----- ---- ---- -----')
        print(f'\n--- Pointer ---')
        print(f'Index: {self.pointer.getIndex()}')
        
        print(f'\n--- Processor ---')
        print(f'Processor <registers>:')
        for register, value in self.processor.getRegisters().items():
            print(f'{register}: {value}')
        print(f'Processor <IP>: {self.ip.getIndex()}')
        print(f'Processor <flag>: {self.processor.getFlag()}')

        print("\n--- Tabla de Etiquetas ---")
        for label, address in self.lookup_table.items():
            print(f"Etiqueta: {label}, Indice: {address}")

        print("\n--- Instrucciones Parseadas ---")
        for index, instr in enumerate(self.instructions):
            print("Nombre: <" + instr.instruction_name() + ">" + "\nPos: <" + str(index) + ">")

        print("\n--- Instrucciones sin Parsear ---")
        for index, instr in enumerate(self.sourceCodeInstructions):
            print("Instruccion: <" + instr + ">" + "\nPos: <" + str(index) + ">")

