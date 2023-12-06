#!/usr/bin/python3
"""This module implements the HBnB console."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is received."""
        print("")
        return True

    def help_quit(self):
        """Display help message for the quit command."""
        print("Exit the program")

    def help_EOF(self):
        """Display help message for the EOF command."""
        print("Exit the program when EOF is received")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
