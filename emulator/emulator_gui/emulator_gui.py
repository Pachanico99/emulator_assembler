import os
from emulator.config.config import Config
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from emulator.processor.processor import Processor

class EmulatorCLI:
    def __init__(self):
        self.scroll_offset = 0
        
        self.screen_height = 25
        self.left_col_width = 30
        self.code_col_width = 50

        self.COLOR_YELLOW = "\033[93m"   
        self.COLOR_RESET = "\033[0m"    # Blanco
        if os.name == 'nt':
            os.system('')

    def get_processor_state_lines(self, processor: "Processor"):
        
        q_instructions = len(processor.get_process().get_runnable().get_instructions())
        state_lines = []
        state_lines.append("Archivo: ")
        state_lines.append(processor.get_process().get_runnable().get_file_name())
        state_lines.append("=" * self.left_col_width)
        state_lines.append("Estado del procesador:")
        state_lines.append(f" IP: {processor.get_ip().get_index()}")
        state_lines.append(f" Status: {processor.get_status().value}")
        state_lines.append(f" Flag: {processor.get_flag()}")
        state_lines.append(f" Registros:")
        
        for register in Config.get_valid_registers():
            register_value = processor.get_register(register)
            state_lines.append(f"   {register}: {register_value}")

        state_lines.append(" Stack:")
        # Reservo los espacios para "====" y "Cantidad de instrucciones"
        reserved_lines = 3
        max_lines_available = self.screen_height - len(state_lines) - reserved_lines
        stack_to_show = list(reversed(processor.get_process().get_stack()))[:max_lines_available]

        for i, value in enumerate(stack_to_show):
            state_lines.append(f"   {len(processor.get_process().get_stack()) - 1 - i}: {value}")

        state_lines.append("=" * self.left_col_width)
        state_lines.append(" Cantidad de instrucciones:")
        state_lines.append(f" {q_instructions}")

        while len(state_lines) < self.screen_height:
            state_lines.append("")

        return state_lines[:self.screen_height]

    def draw_view(self, processor: "Processor"):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        processor_state_lines = self.get_processor_state_lines(processor)
        instructions = processor.get_process().get_runnable().get_sourceCodeInstructions()
        num_instructions = len(instructions)
        current_ip_to_execute = processor.get_ip().get_index()

        if num_instructions > self.screen_height:
            if current_ip_to_execute >= self.scroll_offset + self.screen_height:
                self.scroll_offset = current_ip_to_execute - self.screen_height + 1
            elif current_ip_to_execute < self.scroll_offset:
                self.scroll_offset = current_ip_to_execute
            self.scroll_offset = max(0, min(self.scroll_offset, num_instructions - self.screen_height))
        else:
            self.scroll_offset = 0
        
        header_left_equals = "=" * 30
        header_spacing = " " * 10
        header_text = f"{header_left_equals}{header_spacing}--- Codigo fuente ---"
        print(header_text)

        for i in range(self.screen_height):
            left_part = processor_state_lines[i]
            left_part_padded = f"{left_part:<{self.left_col_width}}"

            right_part_display = ""
            code_line_index_in_source = self.scroll_offset + i

            if 0 <= code_line_index_in_source < num_instructions:
                instr_obj = instructions[code_line_index_in_source]
                raw_line_text = instr_obj.source if hasattr(instr_obj, 'source') else str(instr_obj)
                
                prefix_code = "     "
                color_code = self.COLOR_RESET

                if code_line_index_in_source == current_ip_to_execute:
                    color_code = self.COLOR_YELLOW
                    prefix_code = ">>>  "
                
                available_width_for_text = self.code_col_width - len(prefix_code)
                display_line_text = raw_line_text
                if len(raw_line_text) > available_width_for_text:
                    display_line_text = raw_line_text[:available_width_for_text - 3] + "..."
                
                temp_right_part = f"{prefix_code}{display_line_text}"
                right_part_display = f"{color_code}{temp_right_part:<{self.code_col_width}}{self.COLOR_RESET}"
            else:
                right_part_display = " " * self.code_col_width

            print(f"{left_part_padded}| {right_part_display}")
