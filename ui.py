from utils import clear_screen
import sys


class Command_parser:
    def __init__(self, input, menu, pass_gen):
        self.input = input.strip().lower() if input else None
        self.menu = menu
        self.pass_gen = pass_gen

    def parse_command(self):
        if self.menu.menu == "main_menu":
            if self.input == "1":
                self.input = None
                self.menu.pass_gen_menu()
            if self.input == "2":
                self.input = None
                self.menu.saved_pass_menu()
            if self.input == "3":
                sys.exit()

        if self.menu.menu == "pass_gen_menu":
            if self.input == "1":
                self.input = None
                password = self.pass_gen.create_password_num_let()
                self.menu.new_pass_menu(password)
            if self.input == "2":
                self.input = None
                password = self.pass_gen.create_password_num_let_sym()
                self.menu.new_pass_menu(password)
            if self.input == "3":
                self.input = None
                self.menu.main_menu()

        if self.menu.menu == "saved_pass_menu":
            if self.input:
                self.input = None
                self.menu.main_menu()

    def update_input(self, new_input):
        self.input = new_input.strip().lower()


class Menus:
    def __init__(self, pass_gen):
        self.menu = "main_menu"
        self.pass_gen = pass_gen

    def main_menu(self):
        self.menu = "main_menu"
        clear_screen()
        print("=== HOTCRSSBUNS' PASS MANAGER ===")
        print("\n1. Generate new password")
        print("2. View saved passwords")
        print("3. Exit")
        print("\nChoose an option (1-3):")

    def pass_gen_menu(self):
        self.menu = "pass_gen_menu"
        clear_screen()
        print("=== Password Generator ===")
        print(f"\nPassword length (8-16 characters): {self.pass_gen.pass_length}")
        print("\nInclude:")
        print("1. Letters and Numbers (e.g., ab12CD34)")
        print("2. Letters, Numbers, and Symbols (e.g., ab12#$CD)")
        print("3. Back to main menu")
        print("\nChoose option (1-2):")

    def saved_pass_menu(self):
        self.menu = "saved_pass_menu"
        clear_screen()
        print("=== Saved Passwords===\n")
        try:
            f = open("passwords.txt", "r")
            print(f.read())
            print("Type '1' to go back to main menu")
        except FileNotFoundError:
            print("No passwords found. Try making some!")
            print("Type '1' to go back to main menu")

    def new_pass_menu(self, password):
        self.menu = "new_pass_menu"
        clear_screen()
        print(f"\nYour new password is: {password}")
        choice = input("\nWould you like to save this password? (y/n): ")
        if choice == "y":
            website = input("Enter website or app name: ")
            username = input("Enter username: ")
            f = open("passwords.txt", "a")
            f.write(f"App: {website}\nUsername: {username}\nPassword: {password}\n")
            f.close()
            input(f"\nPassword saved succesfully! (Press enter to return to menu)")
            self.main_menu()
        if choice == "n":
            self.pass_gen_menu()
