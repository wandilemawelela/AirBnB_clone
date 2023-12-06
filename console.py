#!/usr/bin/python3
"""This module implements the HBnB console."""

import cmd
import uuid
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is received."""
        print("")  # Ensure a newline is printed before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def help_quit(self):
        """Display help message for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Display help message for the EOF command."""
        print("Exit the program when EOF is received")

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            global_namespace = globals()

        if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
            print("** class doesn't exist **")
        else:
            new_instance = global_namespace[class_name]()
            new_instance.id = str(uuid.uuid4())  # Set the id attribute with a unique identifier
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def set_prompt(self, new_prompt):
        """Set a new prompt dynamically."""
        self.prompt = f"({new_prompt}) "

    def precmd(self, line):
        """Called just before executing a command."""
        return line

    def postcmd(self, stop, line):
        """Called just after executing a command."""
        if not stop:
            print("")  # Add a newline after each command
        return stop

    def cmdloop(self):
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            print("\nExiting the HBnB console. Goodbye!")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
