from utils import clear_screen
import sys


class Command_parser:
    def __init__(self, input, menu):
        self.input = input.strip().lower()
        self.menu = menu

    def parse_command(self):
        if self.menu.menu == "main_menu":
            if input == "1":
                self.menu.pass_gen_menu()
            if input == "2":
                self.menu.saved_pass_menu()
            if input == "3":
                sys.exit()


class Menus:
    def __init__(self):
        self.menu = "main_menu"

    def main_menu(self):
        self.menu = "main_menu"
        clear_screen()
        print("Welcome to hotcrssbuns' Password Manager!")
        print("\n1. Generate new password")
        print("2. View saved passwords")
        print("3. Exit")
        print("\nChoose an option (1-3)")

    def pass_gen_menu(self):
        self.menu = "pass_gen_menu"
        clear_screen()
        print("=== Password Generator ===")
        print("\nInclude:")
        print("1. Letters and Numbers (e.g., ab12CD34)")
        print("2. Letters, Numbers, and Symbols (e.g., ab12#$CD)")
        print("\nChoose option (1-2):")

    def saved_pass_menu(self):
        self.menu = "saved_pass_menu"
        clear_screen()
        print("=== Saved Passwords===")
