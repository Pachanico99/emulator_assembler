# --- Configuración archivos de entrada y salida --- #
INPUT_FILE = "./files/test2.asm"

# --- Configuración de Validaciones --- # 
VALID_REGISTERS = ["ax", "bx", "cx", "dx"]                                  # Registros valido
INSTRUCTION_SET = ["mov", "add", "inc", "jmp", "jnz", "cmp", "dec"]         # Instrucciones validas
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
        return " | ".join(VALID_REGISTERS)

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