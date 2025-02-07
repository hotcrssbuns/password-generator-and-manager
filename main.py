from utils import clear_screen
from ui import Command_parser
from ui import Menus


def main():
    menu = Menus()
    menu.main_menu()
    while True:
        choice = input("\n> ")
        parser = Command_parser(choice, menu)
        parser.parse_command()


main()
