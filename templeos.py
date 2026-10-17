# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# Цвета TempleOS (16 цветов)
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_WHITE = '\033[1;37m'
    BRIGHT_RED = '\033[1;31m'
    BRIGHT_GREEN = '\033[1;32m'
    BRIGHT_YELLOW = '\033[1;33m'
    BRIGHT_BLUE = '\033[1;34m'
    BRIGHT_MAGENTA = '\033[1;35m'
    BRIGHT_CYAN = '\033[1;36m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_color(text, color):
    print(f"{color}{text}{Colors.RESET}")

def trumpet_sound():
    for freq in [523, 659, 784, 1047]:
        print(f"{Colors.BRIGHT_YELLOW}~ {freq}Hz ~{Colors.RESET}", end='', flush=True)
        time.sleep(0.1)
    print()

def divine_message():
    messages = [
        "Голос с Небес: 64 - священное число!",
        "Божественное откровение: Ты создан по образу и подобию",
        "Мудрость: Истина в простоте, простота в истине",
        "Откровение: 640x480 - идеальное разрешение",
        "Божественный шёпот: Не используй float, используй int",
        "Пророчество: 64 бита - будущее вычислений",
        "Мудрость Соломона: Начало мудрости - страх Господень",
        "Откровение: TempleOS - храм вычислений",
    ]
    return random.choice(messages)

def boot_sequence():
    clear_screen()
    print_color("TempleOS Console Simulation", Colors.BRIGHT_CYAN)
    print_color("=" * 60, Colors.CYAN)
    time.sleep(0.5)
    
    boot_messages = [
        "BIOS Date 01/01/64 14:23:51 Ver: 1.0.64",
        "CPU: HolyC Processor @ 64 GHz",
        "64 GB ECC Memory OK",
        "Detecting primary master ... TEMPLE HDD 64GB",
        "Detecting primary slave  ... None",
        "Starting TempleOS...",
        "Loading HolyC Kernel v6.4.64...",
        "Initializing 64-bit architecture...",
        "Mounting Temple File System...",
        "Loading divine parameters...",
        "Connecting to Heavenly Network...",
        "TempleOS booted successfully!",
    ]
    
    for msg in boot_messages:
        print_slow(msg, 0.01)
        time.sleep(0.1)
    
    time.sleep(1)
    clear_screen()
    trumpet_sound()
    print_color(divine_message(), Colors.BRIGHT_YELLOW)
    time.sleep(2)

class HolyCInterpreter:
    def __init__(self):
        self.variables = {}
        
    def execute(self, code):
        code = code.strip()
        if not code or code.startswith('//'):
            return
            
        if code.startswith('Print(') and code.endswith(')'):
            value = code[6:-1]
            if value.startswith('"') and value.endswith('"'):
                print(value[1:-1])
            elif value in self.variables:
                print(self.variables[value])
            else:
                try:
                    print(eval(value, {"__builtins__": {}}, self.variables))
                except:
                    print(f"Error: Cannot evaluate {value}")
            return
            
        if '=' in code and not code.startswith('If') and not code.startswith('For'):
            parts = code.split('=', 1)
            var_name = parts[0].strip()
            var_value = parts[1].strip()
            
            if var_value.startswith('"') and var_value.endswith('"'):
                self.variables[var_name] = var_value[1:-1]
            else:
                try:
                    self.variables[var_name] = eval(var_value, {"__builtins__": {}}, self.variables)
                except:
                    print(f"Error: Cannot assign {var_value}")
            return
            
        print("HolyC: Command executed")

class TempleOS:
    def __init__(self):
        self.bible_chapters = {}
        self.current_chapter = 0
        self.holyc = HolyCInterpreter()
        self.running = True
        
    def show_main_menu(self):
        clear_screen()
        print_color("=" * 60, Colors.BRIGHT_CYAN)
        print_color("       TEMPLEOS CONSOLE SIMULATION", Colors.BRIGHT_CYAN)
        print_color("=" * 60, Colors.BRIGHT_CYAN)
        print()
        print_color("1. HolyC Interpreter", Colors.GREEN)
        print_color("2. Write The Holy Bible", Colors.GREEN)
        print_color("3. Read The Holy Bible", Colors.GREEN)
        print_color("4. Divine Messages", Colors.GREEN)
        print_color("5. Temple Calculator", Colors.GREEN)
        print_color("6. System Information", Colors.GREEN)
        print_color("7. Trumpet Sound", Colors.GREEN)
        print_color("0. Exit", Colors.RED)
        print()
        print_color("-" * 60, Colors.CYAN)
        return input("Choice: ")
        
    def holyc_interpreter(self):
        clear_screen()
        print_color("HolyC Interpreter v6.4.64", Colors.BRIGHT_YELLOW)
        print_color("Type 'exit' to return", Colors.WHITE)
        print_color("-" * 40, Colors.CYAN)
        
        while self.running:
            try:
                code = input("HolyC> ")
                if code.lower() == 'exit':
                    break
                self.holyc.execute(code)
            except KeyboardInterrupt:
                break
                
    def write_bible(self):
        clear_screen()
        print_color("Writing The Holy Bible...", Colors.BRIGHT_YELLOW)
        print_color("Type your chapter (or 'exit' to return)", Colors.WHITE)
        print()
        
        while self.running:
            try:
                chapter_num = input("Chapter [1-64]: ")
                if chapter_num.lower() == 'exit':
                    break
                    
                try:
                    chapter_num = int(chapter_num)
                    if chapter_num < 1 or chapter_num > 64:
                        print("Chapter must be between 1 and 64!")
                        continue
                except:
                    print("Invalid chapter number!")
                    continue
                    
                print(f"Writing Chapter {chapter_num}...")
                print("Enter text (end with 'END' on a new line):")
                
                lines = []
                while True:
                    line = input()
                    if line == 'END':
                        break
                    lines.append(line)
                    
                self.bible_chapters[chapter_num] = '\n'.join(lines)
                print_color(f"Chapter {chapter_num} saved!", Colors.GREEN)
                time.sleep(1)
                
            except KeyboardInterrupt:
                break
                
    def read_bible(self):
        clear_screen()
        if not self.bible_chapters:
            print_color("The Bible is empty. Write some chapters first!", Colors.YELLOW)
            input("Press Enter to continue...")
            return
            
        print_color("The Holy Bible", Colors.BRIGHT_YELLOW)
        print_color(f"Chapters: {', '.join(map(str, self.bible_chapters.keys()))}", Colors.WHITE)
        print()
        
        while self.running:
            try:
                chapter_num = input("Read chapter [number or 'back']: ")
                if chapter_num.lower() == 'back':
                    break
                    
                try:
                    chapter_num = int(chapter_num)
                    if chapter_num in self.bible_chapters:
                        print_color(f"\n--- Chapter {chapter_num} ---", Colors.BRIGHT_CYAN)
                        print(self.bible_chapters[chapter_num])
                        print()
                    else:
                        print(f"Chapter {chapter_num} not found!")
                except:
                    print("Invalid chapter number!")
                    
            except KeyboardInterrupt:
                break
                
    def divine_messages(self):
        clear_screen()
        print_color("Receiving divine messages...", Colors.BRIGHT_YELLOW)
        time.sleep(1)
        
        for i in range(3):
            print()
            print_color(divine_message(), Colors.BRIGHT_GREEN)
            time.sleep(2)
            
        print_color("\nPress Enter to continue...", Colors.WHITE)
        input()
        
    def calculator(self):
        clear_screen()
        print_color("Temple Calculator (Integer Only - No Float!)", Colors.BRIGHT_YELLOW)
        print_color("Operations: +, -, *, /, %", Colors.WHITE)
        print_color("Type 'exit' to return", Colors.WHITE)
        print()
        
        while self.running:
            try:
                expr = input("Calc> ")
                if expr.lower() == 'exit':
                    break
                    
                if expr in ('+', '-', '*', '/', '%'):
                    a = int(input("First number: "))
                    b = int(input("Second number: "))
                    
                    if expr == '+':
                        result = a + b
                    elif expr == '-':
                        result = a - b
                    elif expr == '*':
                        result = a * b
                    elif expr == '/':
                        if b == 0:
                            print("Error: Division by zero!")
                            continue
                        result = a // b
                    elif expr == '%':
                        if b == 0:
                            print("Error: Division by zero!")
                            continue
                        result = a % b
                        
                    print_color(f"Result: {result}", Colors.GREEN)
                    print_color(f"Binary: {bin(result)}", Colors.CYAN)
                    print_color(f"Hex: {hex(result)}", Colors.MAGENTA)
                    
                else:
                    try:
                        result = eval(expr, {"__builtins__": {}}, {})
                        if isinstance(result, float):
                            print_color("Error: TempleOS does not support float!", Colors.RED)
                            print_color("Use integer arithmetic only!", Colors.YELLOW)
                        else:
                            print_color(f"Result: {result}", Colors.GREEN)
                    except:
                        print("Error: Invalid expression!")
                        
            except KeyboardInterrupt:
                break
            except ValueError:
                print("Error: Please enter integers only!")
                
    def system_info(self):
        clear_screen()
        print_color("=" * 60, Colors.BRIGHT_CYAN)
        print_color("       TEMPLEOS SYSTEM INFORMATION", Colors.BRIGHT_CYAN)
        print_color("=" * 60, Colors.BRIGHT_CYAN)
        print()
        print_color(f"OS: TempleOS Console Simulation", Colors.WHITE)
        print_color(f"Version: 6.4.64", Colors.WHITE)
        print_color(f"Architecture: 64-bit HolyC", Colors.WHITE)
        print_color(f"Kernel: Temple Kernel v6.4.64", Colors.WHITE)
        print_color(f"Memory: 64 GB ECC", Colors.WHITE)
        print_color(f"Resolution: 640x480x16", Colors.WHITE)
        print_color(f"File System: TempleFS", Colors.WHITE)
        print_color(f"CPU: HolyC Processor @ 64 GHz", Colors.WHITE)
        print()
        print_color(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}", Colors.WHITE)
        print_color("Blessed by the Divine Number 64", Colors.BRIGHT_YELLOW)
        print()
        print_color("Bible Chapters Written:", Colors.GREEN)
        if self.bible_chapters:
            for chap in self.bible_chapters:
                print_color(f"  Chapter {chap}", Colors.GREEN)
        else:
            print_color("  None", Colors.WHITE)
        print()
        print_color("Press Enter to continue...", Colors.WHITE)
        input()

def main():
    system = TempleOS()
    boot_sequence()
    
    while system.running:
        choice = system.show_main_menu()
        
        if choice == '1':
            system.holyc_interpreter()
        elif choice == '2':
            system.write_bible()
        elif choice == '3':
            system.read_bible()
        elif choice == '4':
            system.divine_messages()
        elif choice == '5':
            system.calculator()
        elif choice == '6':
            system.system_info()
        elif choice == '7':
            clear_screen()
            trumpet_sound()
            print_color("The trumpet of Gabriel sounds!", Colors.BRIGHT_YELLOW)
            time.sleep(2)
        elif choice == '0':
            clear_screen()
            print_color("TempleOS shutting down...", Colors.YELLOW)
            print_color("God bless you!", Colors.BRIGHT_GREEN)
            time.sleep(1)
            system.running = False
        else:
            print_color("Invalid choice!", Colors.RED)
            time.sleep(1)

if __name__ == "__main__":
    main()
