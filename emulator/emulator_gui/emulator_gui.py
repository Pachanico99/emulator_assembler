import os
import time
from emulator.processor.processor import Processor
from emulator.config.config import Config

class EmulatorCLI:
    def __init__(self, processor: Processor):
        self.running = True
        self.paused = False
        self.scroll_offset = 0
        
        self.screen_height = 30
        self.left_col_width = 30
        self.code_col_width = 50

        self.auto_run_interval_seconds = 0.12
        self.processor = processor

        self.COLOR_YELLOW = "\033[93m"   
        self.COLOR_RESET = "\033[0m"    # Blanco
        if os.name == 'nt':
            os.system('')

    def get_processor_state_lines(self):
        state_lines = []
        state_lines.append("Estado del procesador:")
        state_lines.append(f" IP: {self.processor.ip.get_index()}")
        state_lines.append(f" Flag: {self.processor.get_flag()}")
        state_lines.append(" Registros:")
        
        for register in Config.get_valid_registers():
            register_value = self.processor.get_register(register)
            state_lines.append(f"   {register}: {register_value}")
        
        state_lines.append("=" * self.left_col_width)

        while len(state_lines) < self.screen_height:
            state_lines.append("")
        return state_lines[:self.screen_height]

    def draw_view(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        processor_state_lines = self.get_processor_state_lines()
        instructions = self.processor.runnable.sourceCodeInstructions
        num_instructions = len(instructions)
        current_ip_to_execute = self.processor.ip.get_index()

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

    def run(self):
        try:
            while self.running: 

                current_ip = self.processor.ip.get_index()
                num_instructions = len(self.processor.runnable.sourceCodeInstructions)
                
                if not self.paused and current_ip < num_instructions and self.running:
                    time.sleep(self.auto_run_interval_seconds)
                    self.draw_view()
                    self.processor.step()
                elif self.paused and self.running:
                    pass 
                elif current_ip >= num_instructions:
                    self.running = False

        finally:
            print("Terminando el emulador...")
