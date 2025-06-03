from emulator.instruction.mov import Mov
from emulator.instruction.add import Add
from emulator.instruction.inc import Inc
from emulator.instruction.jmp import Jmp
from emulator.instruction.jnz import Jnz
from emulator.instruction.cmp import Cmp
from emulator.instruction.dec import Dec
from emulator.instruction.noop import Noop
from emulator.instruction.push import Push
from emulator.instruction.pop import Pop
from emulator.instruction.call import Call
from emulator.instruction.ret import Ret

# --- Configuración archivos de entrada y salida --- #
INPUT_FILE = './files/funciones-main.asm'

# --- Configuración de Validaciones --- # 
VALID_REGISTERS = ["ax", "bx", "cx", "dx"]                                  # Registros valido
INSTRUCTION_SET = [                                                         # Instrucciones validas
    Mov.instruction_name(),
    Add.instruction_name(),
    Inc.instruction_name(),
    Jmp.instruction_name(),
    Jnz.instruction_name(),
    Cmp.instruction_name(),
    Dec.instruction_name(),
    Noop.instruction_name(),
    Push.instruction_name(),
    Pop.instruction_name(),
    Call.instruction_name(),
    Ret.instruction_name()
]                                   
LABEL_MAIN_NAME = "main"                                                    # Etiqueta principal
COMMENT_SYMBOLS = ['#',';']                                                 # Simbolos de comentario

import re
class Config:

    @staticmethod
    def get_input_file() -> str:
        return INPUT_FILE

    @staticmethod
    def get_valid_registers() -> list[str]:
        return VALID_REGISTERS

    @staticmethod
    def get_valid_registers_pattern() -> str:
        return "|".join(VALID_REGISTERS)

    @staticmethod
    def get_valid_instruction_names() -> list[str]:
        return INSTRUCTION_SET

    @staticmethod
    def get_valid_instruction_pattern() -> str:
        return "|".join(INSTRUCTION_SET)

    @staticmethod
    def get_label_main_name() -> str:
        return LABEL_MAIN_NAME

    @staticmethod
    def get_comment_symbols_pattern() -> str:
        return re.escape(''.join(COMMENT_SYMBOLS))

    @staticmethod
    def get_comment_symbols() -> list[str]:
        return COMMENT_SYMBOLS

    @staticmethod
    def get_auto_run_interval_seconds() -> int:
        return 1