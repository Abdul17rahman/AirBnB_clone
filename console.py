#!/usr/bin/python3

"""
    Console Module - Entry Point
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        This is class implements all our console commands
    """
    prompt = "(hbnb) "

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
