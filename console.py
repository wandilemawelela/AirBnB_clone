#!/usr/bin/python3
"""This module implements the HBnB console."""

import cmd
import uuid
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is received.
        """
        print("")  # Ensure a newline is printed before exiting
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Display help message for the quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help message for the EOF command.
        """
        print("Exit the program when EOF is received")

    def do_create(self, arg):
        """
        Usage: create <class>

        Create a new class instance and print its id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        # Check if the class exists in the global namespace
        global_namespace = globals()
        if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
            # If the class doesn't exist, print an error message
            print("** class doesn't exist **")
            return

        # The class exists, proceed with creating an instance
        new_instance = global_namespace[class_name]()
        new_instance.id = str(uuid.uuid4())
        new_instance.save()  # This line saves the instance to storage

        # Debug print statement to check if the instance is saved
        print(f"Instance saved to storage: {new_instance}")

        print(new_instance.id)
              
    def do_show(self, arg):
        """
        Usage: show <class> <id>

        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            class_name = args[0]
            global_namespace = globals()
            if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            global_namespace = globals()
            if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                all_instances = storage.all()
                # print(f"All instances: {all_instances}")  # Debug statement
                if key in all_instances:
                    print(all_instances[key])  # Print the instance itself
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id>
        
        Deletes an instance based on the class name and ID
        (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            global_namespace = globals()

            if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                    # print(f"Instance deleted: {class_name} - {instance_id}") Debug statement
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Usage: all [<class>]
        
        Prints all string representation of all instances based or not on the class name.
        """
        args = arg.split()
        object_list = []

        if len(args) == 0:
            for key, obj in storage.all().items():
                object_list.append(str(obj))
            print(object_list)
        else:
            class_name = args[0]
            global_namespace = globals()

            if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
                print("** class doesn't exist **")
            else:
                for key, obj in storage.all().items():
                    if key.split('.')[0] == class_name:
                        object_list.append(str(obj))
                print(object_list)

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        
        Updates an instance based on the class name and ID by adding or updating
        an attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            global_namespace = globals()

            if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    obj = storage.all()[key]
                    # Check if the attribute exists and is updateable
                    if hasattr(obj, attribute_name) and attribute_name not in ['id', 'created_at', 'updated_at']:
                        # Update the attribute with the casted value
                        setattr(obj, attribute_name, type(getattr(obj, attribute_name))(attribute_value))
                        obj.save()
                        # print(f"Attribute updated: {class_name} - {instance_id} - {attribute_name} - {attribute_value}") Debug statement
                    else:
                        print("** attribute name not found or not updateable **")
                else:
                    print("** no instance found **")

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
    # Ensure storage is an instance of FileStorage
    if not isinstance(storage, FileStorage):
        storage = FileStorage()

    # Load existing objects from the JSON file
    storage.reload()

    HBNBCommand().cmdloop()
