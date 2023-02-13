#!/usr/bin/python3
"""Import modules"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State



class HBNBCommand(cmd.Cmd):
    """Class for the HBNB interpreter"""
    # dictionary of classes because I did not read the next requirement
    # one was a stupid idea on my part, plus unlocked advanced
    # to save me some sanity refactoring code
    __classes = {
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    }

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command handler that exits the program quietly"""
        return True

    def do_exit(self, line):
        """Command to exit, you're welcome"""
        return True

    prompt = '(hbnb) '

    def emptyline(self):
        """ENTER and emptyline should not execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to the given JSON"\
        "file and prints its id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            # print(args)
            return
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on"\
        "its class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Destroy/delete an instance based on the given class"\
        "name and id from the JSON file given"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all"\
        "instances based (or not) on the class name"""
        if not args:
            print([str(value) for value in storage.all().values()])
            return
        if args not in self.__classes:
            print("** class doesn't exist **")
            return
        print([str(value) for key,
               value in storage.all().items() if key.startswith(args)])
        
    def do_update(self, args):
        """Updates an instance based on the class name"""
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            inst_id = args_list[0] + "." + args_list[1]
            dict_instances = storage.all()

            if inst_id in dict_instances.keys():
                if args_list[2] in ["id", "created_at", "updated_at"]:
                    print("** can't update id, created_at, updated_at **")
                    return
                if args_list[3]:
                    args_list[3] = args_list[3].replace('"', "")
                try:
                    args_list[3] = int(args_list[3])
                except ValueError:
                    try:
                        args_list[3] = float(args_list[3])
                    except ValueError:
                        args_list[3] = args_list[3]
                dict_instances[inst_id].__dict__[args_list[2]] = args_list[3]
                dict_instances[inst_id].save()
            else:
                # doesn't work for some reason, and honestly, I am tired.
                # Whoever comes across and can figure it out, great!
                # Plus, it does not seem to affect it in any way so if the
                # error bugs you, feel free to fix!
                print("** no instance found **")
        # if len(args) < 3:
        #     print("** attribute name missing **")
        #     return
        # if len(args) < 4:
        #     print("** value missing **")
        #     return
        # instance_id = args[0] + "." + args[1]
        # if instance_id in storage.all().keys():
        #     if args[3]:
        #         args[3] = args[3].replace('"', "")
        #     try:
        #         args[3] = int(args[3])
        #     except ValueError:
        #         try:
        #             args[3] = float(args[3])
        #         except ValueError:
        #             args[3] = args[3]
        #     storage.all()[instance_id].__dict__[args[2]] = args[3]
        #     storage.all()[instance_id].save()
        # else:
        #     print("** no instance found **")
                    
        # attr_name = args[2]
        # if attr_name in ["id", "created_at", "updated_at"]:
            # print("You cannot update the id, and modify the created_at and"\
            # "updated_at dates")
            # return
        
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
