from abc_interfaces import UserInterface
from console_interface import ConsoleInterface
from prompt_toolkit.completion import WordCompleter

from show_greeting import greet
from commands import (
    hello,
    helper,
    add_contact,
    del_contact,
    del_phone,
    error_func,
    get_bd,
    del_bd,
    upd_bd,
)
from commands import (
    change_phone,
    show_all,
    good_bye,
    add_phone,
    change_name,
    search_by_name,
    search_by_phone,
    add_bd,
)

cmds = {
    "add": add_contact,  # len(args) >= 2 arg name phone (bd) +
    "add_phone": add_phone,  # len(args) >= 2 arg name phone +
    "del": del_contact,  # len(args) >= 1 arg name +
    "del_bd": del_bd,  # len(args) >= 1 name +
    "upd_bd": upd_bd,  # len(args) >= 2 arg name bd +
    "del_phone": del_phone,  # len(args) >= 2 name phone +
    "change": change_name,  # len(args) >= 2 old_name new_name
    "change_phone": change_phone,  # len(args) >= 2 name new_phone +
    "add_bd": add_bd,  # len(args) >= 2 arg name bd +
    "get_bd": get_bd,  # len(args) >= 1 arg name +
    "name": search_by_name,  #  +
    "phone": search_by_phone,  #  +
}

simple_cmds = {
    "show all": show_all,
    "good bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye,
    "help": helper,
    "hello": hello,
}


def main(user_interface: UserInterface):
    while True:
        usr_inp = user_interface.get_user_input()
        if usr_inp in simple_cmds.keys():
            s_func = simple_cmds[usr_inp.strip()]
            user_interface.display_output(s_func())
        elif not usr_inp or usr_inp.split()[0] not in cmds.keys():
            user_interface.display_output(error_func())
        else:
            if usr_inp.split()[0] in cmds.keys() and len(usr_inp.split()) > 1:
                command, *data = usr_inp.strip().split(" ", 1)
                handler = cmds[command]
                args = data[0].split(" ")
                user_interface.display_output(handler(*args))
            else:
                user_interface.display_output(error_func())


if __name__ == "__main__":
    coms = [cmd for dict in [cmds, simple_cmds] for cmd in dict.keys()]
    compl = WordCompleter(coms, ignore_case=True)
    console_interface = ConsoleInterface(compl, False)
    greet()
    main(console_interface)
