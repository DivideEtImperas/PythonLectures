import model
from logger import print_name
import view


def button_click():
    new_initials = view.get_name()
    initials = model.read_name()
    if new_initials == initials:
        print_name()


if __name__ == '__main__':
    button_click()
