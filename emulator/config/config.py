# --- Configuración archivos de entrada y salida --- #
INPUT_FILE = './files/funciones-main.asm'

# --- Configuración de Validaciones --- # 
VALID_REGISTERS = ["ax", "bx", "cx", "dx", "aux"]                                  # Registros valido
                                
LABEL_MAIN_NAME = "main"                                                    # Etiqueta principal
COMMENT_SYMBOLS = ['#',';']                                                 # Simbolos de comentario
QUANTITY_OF_INSTRUCTIONS_PER_BURST = 3                                      # Cantidad de instrucciones por rafaga de ejecucion

VIDEO_MEMORY_WIDTH = 10
VIDEO_MEMORY_HEIGHT = 10

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
    def get_label_main_name() -> str:
        return LABEL_MAIN_NAME

    @staticmethod
    def get_comment_symbols_pattern() -> str:
        return re.escape(''.join(COMMENT_SYMBOLS))

    @staticmethod
    def get_comment_symbols() -> list[str]:
        return COMMENT_SYMBOLS

    @staticmethod
    def get_quantity_of_instructions_per_burst() -> int:
        return QUANTITY_OF_INSTRUCTIONS_PER_BURST

    @staticmethod
    def get_quantity_of_instructions_per_burst_pattern() -> str:
        return str(QUANTITY_OF_INSTRUCTIONS_PER_BURST)

    @staticmethod
    def get_auto_run_interval_seconds() -> int:
        return 0.001
    @staticmethod
    def get_video_memory_width() -> int:
        return VIDEO_MEMORY_WIDTH

    @staticmethod
    def get_video_memory_height() -> int:
        return VIDEO_MEMORY_HEIGHT
