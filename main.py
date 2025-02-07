from utils import clear_screen
from ui import Command_parser
from ui import Menus


def main():
    menu = Menus()
    parser = Command_parser(None, menu)
    menu.main_menu()
    while True:
        choice = input("\n> ")
        parser.update_input(choice)
        parser.parse_command()


main()
