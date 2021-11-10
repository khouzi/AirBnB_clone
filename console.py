#!/usr/bin/python3
"""
console module
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb)"

    classes = {"BaseModel", "User", "Amenity",
               "State", "City", "Place", "Review"}

    def do_quit(self, args):
        """
        exit program
        """
        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_help(self, args):
        """
        help command
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        creates a new instances of BaseModel
        saves it and prints the id
        """
        args = args.split(" ")
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dict_obj = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key in dict_obj:
            print(dict_obj[my_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        dict_obj = storage.all()
        my_key = args[0] + "." + args[1]
        for my_key in dict_obj:
            del dict_obj[my_key]
            storage.save()
            print(storage.all())

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = args.split()
        dict_obj = storage.all()
        l = []
        if len(args):
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in dict_obj.items():
                if class_name in k:
                    l.append((dict_obj[k].__str__()))
        else:
            for k, v in dict_obj.items():
                l.append((dict_obj[k].__str__()))
        print(l)

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if args[1] == "":
            print("** instance id missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
