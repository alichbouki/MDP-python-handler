from lib.addAccount import *

from sys import argv as terminal

class execComand:
    def __init__(self) -> None:
        self.command = terminal[1]
        self.value = terminal[2] 

    def checCommand(self):
        if self.command == "addAccount":
            do = addAccount()
            do.add(self.value)