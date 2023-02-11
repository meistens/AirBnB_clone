#!/usr/bin/python3
"""Import modules"""
import cmd
from models import storage
from models.base_model import BaseModel

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

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to the given JSON file and prints its id"""
        class_name = args.strip()
        if not args:
            print("** class name missing **")
            return
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on its class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Destroy/delete an instance based on the given class name and id from the JSON file given"""
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        args = args.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
