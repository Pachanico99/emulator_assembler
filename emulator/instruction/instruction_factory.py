import re
from typing import List, Dict, Any, Tuple
from emulator.instruction.mov import Mov
from emulator.instruction.add import Add
from emulator.instruction.inc import Inc
from emulator.instruction.jmp import Jmp
from emulator.instruction.jnz import Jnz
from emulator.instruction.cmp import Cmp
from emulator.instruction.dec import Dec
from emulator.instruction.noop import Noop
from emulator.instruction.instruction import Instruction
from emulator.config.config import Config

class InstructionFactory:
    REGISTER_PARAM_TYPE = 'register'
    IMMEDIATE_PARAM_TYPE = 'immediate'
    LABEL_PARAM_TYPE = 'label'
    REGISTER_OR_IMMEDIATE_PARAM_TYPE = 'register_or_immediate'
    INSTRUCTION_SIGNATURES: Dict[str, Tuple[Any, List[str]]] = {
        Mov.instruction_name().lower(): (Mov, [REGISTER_PARAM_TYPE, REGISTER_OR_IMMEDIATE_PARAM_TYPE]),
        Add.instruction_name().lower(): (Add, [REGISTER_PARAM_TYPE, REGISTER_OR_IMMEDIATE_PARAM_TYPE]),
        Inc.instruction_name().lower(): (Inc, [REGISTER_PARAM_TYPE]),
        Dec.instruction_name().lower(): (Dec, [REGISTER_PARAM_TYPE]),
        Jmp.instruction_name().lower(): (Jmp, [LABEL_PARAM_TYPE]),
        Jnz.instruction_name().lower(): (Jnz, [LABEL_PARAM_TYPE]),
        Cmp.instruction_name().lower(): (Cmp, [REGISTER_OR_IMMEDIATE_PARAM_TYPE, REGISTER_OR_IMMEDIATE_PARAM_TYPE]),
    }
    LABEL_FORMAT_PATTERN = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')

    @staticmethod
    def create_instruction(name: str, raw_params: List[str]) -> Instruction:
        if name not in InstructionFactory.INSTRUCTION_SIGNATURES:
             raise Exception(f"Instruccion desconocida: '{name}'")

        instruction_class, expected_types = InstructionFactory.INSTRUCTION_SIGNATURES[name]

        validated_and_converted_params = InstructionFactory.validate_params(name, raw_params, expected_types)

        try:
            return instruction_class(*validated_and_converted_params)
        except TypeError as e:
            raise TypeError(f"Error de tipos al instanciar '{name}' con parametros {validated_and_converted_params}: {e}")
        except Exception as e:
             raise Exception(f"Error al instanciar '{name}' con parametros {validated_and_converted_params}: {e}")

    @staticmethod
    def validate_params(name: str, raw_params: List[str], expected_types: List[str]):
        if len(raw_params) != len(expected_types):
            raise Exception(f"Numero incorrecto de parametros para '{name}': Se esperaban {len(expected_types)}, se encontraron {len(raw_params)}.")

        validated_and_converted_params: List[Any] = []
        for i, param in enumerate(raw_params):
            expected_type = expected_types[i]
            converted_value: Any = None
            param_is_valid = False

            if expected_type == InstructionFactory.REGISTER_PARAM_TYPE:
                if param in Config.get_valid_registers():
                    param_is_valid = True
                    converted_value = str(param) 
                else:
                    raise Exception(f"Parametro {i+1} invalido para '{name}': Se esperaba un registro valido, se encontro '{param}'.")

            elif expected_type == InstructionFactory.IMMEDIATE_PARAM_TYPE:
                if InstructionFactory.is_immediate_format(param):
                    param_is_valid = True
                    converted_value = int(param)
                else:
                    raise Exception(f"Parametro {i+1} invalido para '{name}': Se esperaba un valor numerico inmediato, se encontro '{param}'.")

            elif expected_type == InstructionFactory.LABEL_PARAM_TYPE:
                if InstructionFactory.is_label_format(param):
                     param_is_valid = True
                     converted_value = str(param)
                else:
                     raise Exception(f"Parametro {i+1} invalido para '{name}': Se esperaba una etiqueta valida, se encontro '{param}'.")

            elif expected_type == InstructionFactory.REGISTER_OR_IMMEDIATE_PARAM_TYPE:
                 if param in Config.get_valid_registers():
                     param_is_valid = True
                     converted_value = str(param)
                 elif InstructionFactory.is_immediate_format(param):
                     param_is_valid = True
                     converted_value = int(param)
                 else:
                     raise Exception(f"Parametro {i+1} invalido para '{name}': Se esperaba un registro o un valor inmediato, se encontro '{param}'.")

            else:
                raise Exception(f"Error de configuracion interna: Tipo de parametro esperado desconocido '{expected_type}' para '{name}'.")

            if not param_is_valid:
                 raise Exception(f"Error de validacion inesperado para parametro {i+1} '{param}' en '{name}'.")

            validated_and_converted_params.append(converted_value)

        return validated_and_converted_params

    @staticmethod
    def is_immediate_format(param: str) -> bool:
        if not param: return False
        param_stripped = param.strip()
        if not param_stripped: return False

        if param_stripped[0] in ('-', '+'):
            if len(param_stripped) == 1: return False
            return param_stripped[1:].isdigit()
        return param_stripped.isdigit()

    @staticmethod
    def is_label_format(param: str) -> bool:
        return InstructionFactory.LABEL_FORMAT_PATTERN.fullmatch(param) is not None

    @staticmethod
    def create_noop() -> Noop:
        return Noop()

    