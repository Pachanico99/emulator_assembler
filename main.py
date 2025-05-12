from emulator.assembler.assembler import Assembler
from emulator.processor.processor import Processor
from emulator.emulator_gui.emulator_gui import EmulatorCLI

def main():
    assembler = Assembler()
    runnable = assembler.assemble('./files/test3.asm')
    if runnable is None:
        return
    processor = Processor(runnable.main_index, runnable)
    gui = EmulatorCLI(processor)
    gui.run()
    

if __name__ == "__main__":
    main()