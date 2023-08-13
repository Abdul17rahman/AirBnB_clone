#!/usr/bin/python3

"""
    Console Module - Entry Point
"""

import sys
import inspect
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
        This is class implements all our console commands
    """
    prompt = "(hbnb) "
    cls_mem = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    cls_exist = False

    def do_create(self, arg):
        """ Creates a new instance of a class"""
        if not arg:
            print("** class name missing **")
        else:
            for obj in self.cls_mem:
                if arg == obj[0]:
                    self.cls_exist = True
                    new_inst = obj[1]()
                    models.storage.new(new_inst)
                    models.storage.save()
                    print(new_inst.id)
            if not self.cls_exist:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if not args:
            print("** class name is missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            name = args[0]
            _id = args[1]
            found = False
            all_inst = models.storage.all()
            # Find an instance
            for key, value in all_inst.items():
                if name == value.__class__.__name__:
                    self.cls_exist = True
                    if _id == value.id:
                        found = True
                        print(value)
            if not self.cls_exist:
                print("** class doesn't exist **")
            elif not found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Destroys an instance based on the name and id"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
        elif len(args) == 1:
            print("** instance missing id **")
        else:
            name = args[0]
            _id = args[1]
            all_inst = models.storage.all()
            # Find an instance by looping through all instances
            found_instance = {key: value for key, value in all_inst.items()
                              if name == value.__class__.__name__ and
                              _id == value.id}
            if not found_instance:
                print("** instance not found **")
            # Delete the found instance
            for key in found_instance:
                del all_inst[key]
            models.storage.save()

    def do_all(self, arg):
        """ Prints the string representation of all """
        all_inst = models.storage.all()
        obj_values = []
        for key, value in all_inst.items():
            obj_values.append(value)
        # Print the obj representation
        for obj in obj_values:
            print(obj)

    def do_quit(self, line):
        """ Ends or Quits out of the console"""
        return True

    def emptyline(self):
        """ Does nothing on emty line"""
        pass

    def do_EOF(self, line):
        """ Uses CTRL-D to exit the console"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
