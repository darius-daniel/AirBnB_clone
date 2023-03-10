#!/usr/bin/python3
"""Command interpreter entry point
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Entry point to of the command interpreter
    """
    prompt = "(hbnb) "
    __cls_dict = {"BaseModel": BaseModel}

    def do_EOF(self):
        """Exits the program from non-interactive mode"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        quit()

    def do_create(self, cls):
        """Creates a new instance of a class, saves it to the JSON file,
        and prints the id.

        Args:
            cls: class name
        """
        if not cls:
            print("** class name missing **")
        if cls not in HBNBCommand.__cls_dict:
            print("** class doesn't exit **")
        else:
            new = HBNBCommand.__cls_dict[cls]()
            new.save()
            print(new.id)

    def do_show(self, *args):
        """Prints the string representation of an instance based on the class
        name and id of the instance

        Args:
            cls: class name
            id: id
        """
        arg_list = args[0].split(" ")
        print(arg_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
