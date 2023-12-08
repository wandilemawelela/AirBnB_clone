#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import uuid
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>

        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return

        class_name = argl[0]

        # Check if the class exists in the global namespace
        global_namespace = globals()
        if class_name not in global_namespace or not isinstance(global_namespace[class_name], type):
            # If the class doesn't exist, print an error message
            print("** class doesn't exist **")
            return

        # The class exists, proceed with creating an instance
        new_instance = global_namespace[class_name]()
        new_instance.save()  # This line saves the instance to storage
        print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of a class instance."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif len(argl) == 1:
            class_name = argl[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            class_name = argl[0]
            instance_id = argl[1]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                all_instances = storage.all()
                if key in all_instances:
                    print(all_instances[key])  # Print the instance itself
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])
            key = "{}.{}".format(argl[0], argl[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Display string representations of all instances."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance by adding or updating attributes."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            # Check if the value is a dictionary
            if argl[2][0] == '{':
                try:
                    value_dict = eval(argl[2])
                    if not isinstance(value_dict, dict):
                        print("** invalid dictionary syntax **")
                        return False
                except Exception:
                    print("** invalid dictionary syntax **")
                    return False
            else:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            # Check if the attribute exists in the class or as a property
            if hasattr(obj, argl[2]):
                setattr(obj, argl[2], type(getattr(obj, argl[2]))(argl[3]))
                obj.save()  # Save the changes made to the object
            else:
                print("** attribute name not found or not updateable **")
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if hasattr(obj, k):
                    setattr(obj, k, type(getattr(obj, k))(v))
                else:
                    obj.__dict__[k] = v
            obj.save()  # Save the changes made to the object

if __name__ == "__main__":
    HBNBCommand().cmdloop()

