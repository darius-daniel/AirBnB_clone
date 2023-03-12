#!/usr/bin/python3
"""Command interpreter entry point
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Entry point to of the command interpreter
    """
    prompt = "(hbnb) "
    __cls_dict = {"BaseModel": BaseModel, "User": User,
                  'Amenity': Amenity, 'City': City,
                  'Place': Place, 'Review': Review, 'State': State
                  }

    @staticmethod
    def check(line):
        """Checks is class name and instance ids have been passed to the
        command. If they have been passed, it also checks if the exist
        """
        if not line:
            print("** class name missing **")
            return False

        arg_list = line.split(" ")
        if arg_list[0] and arg_list[0] not in HBNBCommand.__cls_dict.keys():
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        return True

    def help_help(self):
        print("Displays information about commands")

    def do_EOF(self):
        """Exits the program from non-interactive mode"""
        return True

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        return True

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

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id of the instance

        Args:
            line: a string
        """
        if self.check(line):
            found = False
            arg_list = line.split(" ")
            obj_dict = storage.all()

            for key in obj_dict.keys():
                id = key.split(".")[1]
                if id == arg_list[1]:
                    found = True
                    break

            if found:
                print(obj_dict[key].__str__())
            else:
                print("** no instance found **")

    def emptyline(self):
        """Overrides the default behaviour of the builtin emptyline() method,
        making it to do nothing when empty line is passed to command
        interpreter
        """
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id and saves
        the change into the JSON file

        Args:
            line: a string
        """
        if self.check(line):
            found = False
            arg_list = line.split(" ")
            inst_dict = storage.all()

            for key, value in inst_dict.items():
                id = key.split(".")[1]
                if id == arg_list[1]:
                    found = True
                    break

            if found:
                del inst_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all instances based or not on
        the class name.
        """
        if not line:
            print("** class name is missing **")
        elif line in HBNBCommand.__cls_dict:
            inst_dict = storage.all()

            inst_list = []
            for key, value in inst_dict.items():
                k = key.split('.')[0]
                if k == line:
                    inst_list.append(value.__str__())

            print(inst_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute, and save the change into the JSON file

        Args:
            line: a string containing a space-separated list of arguments
        """
        if self.check(line):
            args_list = line.split(" ")
            if len(args_list) < 3:
                print("** attribute name missing **")
                return
            elif len(args_list) < 4:
                print("** value missing **")
                return
            inst_dict = storage.all()

            found = False
            for key, value in inst_dict.items():
                k = key.split('.')
                if k[1] == args_list[1]:
                    setattr(value, args_list[2], args_list[3])
                    storage.save()
                    found = True
                    break

            if not found:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
