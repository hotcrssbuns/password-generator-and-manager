from utils import clear_screen
from ui import Command_parser
from ui import Menus
from password_generator import Password_manager


def main():
    pass_gen = Password_manager()
    menu = Menus(pass_gen)
    parser = Command_parser(None, menu, pass_gen)
    menu.main_menu()
    while True:
        choice = input("\n> ")
        parser.update_input(choice)
        parser.parse_command()


main()
