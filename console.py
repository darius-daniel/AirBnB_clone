#!/usr/bin/python3
"""Command interpreter entry point
"""
import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Entry point to of the command interpreter
    """
    prompt = "(hbnb) "
    __cls_dict = {"BaseModel": BaseModel}

    @staticmethod
    def check(line):
        """Checks is class name and instance ids have been passed to the
        command. If they have been passed, it also checks if the exist
        """
        if not line:
            print("** class name is missing **")
            return False

        arg_list = line.split(" ")
        if arg_list[0] and arg_list[0] not in HBNBCommand.__cls_dict.keys():
            print("** class doesn't exist **")
            return False

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        return True

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

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id of the instance

        Args:
            line: a string
        """
        if self.check(line):
            found = False
            arg_list = line.split(" ")

            with open("file.json", 'r') as file:
                obj_dict = json.load(file)

            for key in obj_dict.keys():
                id = key.split(".")[1]
                if id == arg_list[1]:
                    found = True
                    break

            if found:
                new = HBNBCommand.__cls_dict[arg_list[0]](**obj_dict[key])
                print(new)
            else:
                print("** no instance found **")

    def do_emptyline(self):
        """Overrides the default behaviour of the builtin emptyline() method
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

            with open("file.json", 'r') as file:
                arg_dict = json.load(file)

            for key in arg_dict.keys():
                id = key.split(".")[1]
                if id == arg_list[1]:
                    found = True
                    break

            if found:
                del arg_dict[key]
                with open("file.json", 'w') as file:
                    json.dump(arg_dict, file)
                print(storage.all())
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all instances based or not on
        the class name.
        """
        if not line:
            print("** class name is missing **")
        elif line in HBNBCommand.__cls_dict:
            with open("file.json", 'r') as file:
                inst_dict = json.load(file)

            inst_list = []
            for key, value in inst_dict.items():
                k = key.split('.')[0]
                new = HBNBCommand.__cls_dict[k](**value)
                inst_list.append(new.__str__())

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
            print(args_list)
            if len(args_list) < 3:
                print("** attribute name is missing **")
                return
            elif len(args_list) < 4:
                print("** value missing **")
                return

            with open("file.json", 'r') as file:
                inst_dict = json.load(file)

            key = args_list[0] + '.' + args_list[1]
            inst_dict[key][args_list[2]] = args_list[3]
            print(inst_dict)
            # with open("file.json", 'w') as file:
            #     json.dump(inst_dict, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
