#!/usr/bin/python3
"""Import modules"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Class for the HBNB interpreter"""

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command handler that exits the program quietly"""
        return True

    prompt = '(hbnb) '

    def emptyline(self):
        """ENTER and emptyline should not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
