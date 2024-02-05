#!/usr/bin/python3
"""console to interact with the backend"""

import cmd
from models.base import BaseModel, Base
from models.review import Review
from models.student import Student
from models.subject import Subject
from models.tutor import Tutor

classes = ["Tutor", "Student", "Review", "Subject"]

class Sdcmd(cmd.Cmd):
    """class to define the define the cmd console"""
    prompt = '>>>'

    def do_create(self, arg):
        """creates an instance of an object"""
        args = arg.split()
        if args[0] not in classes:
            return False
        if len(args) != 1:
            print("Usage: <classname>")
            return False
        

    def do_EOF(self, arg):
        """exist console"""
        return True
    
    def emptyline(self) -> bool:
        """overwriting the emptyline method"""
        return False
    
if __name__ == '__main__':
    Sdcmd().cmdloop()