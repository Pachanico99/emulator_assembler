import sys
from emulator.assembler.assembler import Assembler
from emulator.emulator_gui.emulator_gui import EmulatorCLI
from emulator.processor.processor import Processor
from emulator.operating_system.operating_system import OperatingSystem
from emulator.process.process import Process
import time

def main():
    assembler = Assembler()
    runnables = []

    for file_path in sys.argv[1:]:
        runnable = assembler.assemble(file_path)
        # time.sleep(1.5)                                                                 # debug
        # Si se ensamblo correctamente
        if runnable:                                
            runnables.append(runnable)
        else:
            print(f"\n -------------------- ")

    time.sleep(1)                                                                      # debug

    if not runnables:
        print("No se pudo ensamblar ningún archivo.")
        return

    # Creo los procesos
    processes = [Process(runnable=runnable) for runnable in runnables]

    # Creo el CLI y el procesador
    cli = EmulatorCLI()
    processor = Processor(emulator_cli=cli)

    # Creo el sistema operativo con procesos y procesador
    operating_system = OperatingSystem(processes=processes, processor=processor)

    # Seteo el sistema operativo en el procesador
    processor.set_operating_system(operating_system)

    # Seteo el primer proceso
    if processes:
        processor.set_first_process(processes[0])

    processor.process()

if __name__ == "__main__":
    main()

