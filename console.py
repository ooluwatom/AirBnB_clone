#!/usr/bin/python3

'''The cmd module'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''The HBNB command'''

    def do_quit(self, line):
        '''Quit the program'''
        return True

    def do_EOF(self, arg):
        '''Exit the command interpreter'''
        return True

    def do_help(self, arg):
        '''Prints all available commands'''
        cmd.Cmd.do_help(self, arg)

    def do_hbnb(self, arg):
        """
        Prints "Welcome to HBNB", a custom hbnb command
        """
        print("Welcome to HBNB")

    def help_hbnb(self):
        """
        Prints the docstring of the hbnb command
        """
        print(self.do_hbnb.__doc__)

    def emptyline(self):
        '''Returns nothing when there is an empty line'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
