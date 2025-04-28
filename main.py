from emulator.assembler.assembler import Assembler

def main():
    assembler = Assembler()
    assembler.assemble('./files/test2.asm')

if __name__ == "__main__":
    main()