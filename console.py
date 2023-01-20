#!/usr/bin/python3

'''The cmd module'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''The HBNB command'''

    def do_quit(self, command):
        '''Quit the program'''
        exit()

    def help_quit(self):
        '''Documentation for quit'''
        print('Exits the command interpreter \n')

    def do_EOF(self, arg):
        '''Handles EOF to quit the interpreter'''
        print()
        exit()

    def help_quit(self):
        '''Documentation for EOF'''
        print('Exits the command interpreter \n')

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
