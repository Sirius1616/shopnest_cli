#!/usr/bin/python3

import cmd
from domain.base_model import BaseModel
from domain.order import Order
from domain.product import Product
from domain.user import User



classes = {'BaseModel': BaseModel, 'Order': Order, 'Product': Product, 'User': User}


class ShopNestCommand(cmd.Cmd):
    prompt = '(shopnest) '
    

    def do_quit(self, arg):
        """Quit command that exits the program"""


        return True

    def do_EOF(self, arg):
        """Exits the console on the pressing of CTR + D gracefully without an error"""

        print()

    def do_create(self, arg):
        """The ultimate creator of classes"""
        arg_split = arg.split(" ")
        if len(arg_split) = 1:
            print(f"** class name missing **")
        


        return True



if __name__ == '__main__':
    
    ShopNestCommand().cmdloop()
    
 