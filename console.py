#!/usr/bin/python3

'''The cmd module'''
import cmd
import datetime
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''The HBNB command'''

    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, command):
        '''Quit the program'''
        exit()

    def help_quit(self):
        '''Documentation for quit'''
        print('Quit command to exit the program \n')

    def do_EOF(self, arg):
        '''Handles EOF to quit the interpreter'''
        print()
        exit()

    def do_help(self, arg):
        '''Prints all available commands'''
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        '''Returns nothing when there is an empty line'''
        pass

    def do_create(self, class_name):
        '''Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id'''
        bm1 = BaseModel()
        bm1.save()
        if not class_name:
            print('** class name missing **')
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(bm1.id)

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id\n")

    def do_show(self, args):
        '''Prints the string representation of an instance based on the class name and id'''
        new = args.partition (' ')
        class_name = new[0]
        inst_id = new[1]
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not inst_id:
            print("** instance id missing **")
        else:
            key = class_name + "." + inst_id
            try:
                print(storage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        print('Prints the string representation of an instance based on the class name and id')

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id (save the change into the JSON file)'''
        new = args.partition (' ')
        class_name = new[0]
        inst_id = new[1]
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not inst_id:
            print("** instance id missing **")
        else:
            key = class_name + "." + inst_id
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")
    
    def __hash__(self) -> int:
        print("Deletes an instance based on the class name and id (save the change into the JSON file)")

    def do_all(self, args):
        '''Prints all string representation of all instances based or not on the class name'''
        new = args.partition(' ')
        class_name = new[0]
        list = []
        if not class_name:
            for key in storage._FileStorage__objects:
                list.append(storage._FileStorage__objects[key].__str__())
            print(list)
        if class_name:
            if class_name in HBNBCommand.classes:
                for key in storage._FileStorage__objects:
                    if str(key).startswith(class_name):
                        list.append(storage._FileStorage__objects[key].__str__())
                print(list)
            elif class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")

    def help_all(self):
        print('Prints all string representation of all instances based or not on the class name')

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)'''
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                storage.save()

    def help_update(self):
        print('Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)')
        print('Usage: update <class name> <id> <attribute name> "<attribute value>"')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
