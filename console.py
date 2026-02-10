#!/usr/bin/python3

import cmd



class ShopNestCommand(cmd.Cmd):
    prompt = '(shopnest) '
    

    def do_quit(self, arg):
        """This is the method that exits the console CLI"""


        return True

    def do_EOF(self):
        """Exits the console on the pressing of CTR + D gracefully without an error"""

        return True



if __name__ == '__main__':
    ShopNestCommand().cmdloop()
    