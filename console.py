#!/usr/bin/python3

import cmd
from domain.base_model import BaseModel
from domain.order import Order
from domain.product import Product
from domain.user import User
from domain import storage





class ShopNestCommand(cmd.Cmd):
    prompt = '(shopnest) '

    classes = {'BaseModel': BaseModel, 'Order': Order, 'Product': Product, 'User': User}

    

    def do_quit(self, arg):
        """Quit command that exits the program"""


        return True

    def do_EOF(self, arg):
        """Exits the console on the pressing of CTR + D gracefully without an error"""

        print()

    def do_create(self, arg):
        """The ultimate creator of classes"""
        if not arg:
            print("** Class name missing **")
            return True

        arg_split = arg.split(" ")
        if len(arg_split) > 0:
            if arg_split[0] not in ShopNestCommand.classes:
                print("class name does not exist")
            else:
                new_obj = ShopNestCommand.classes[arg_split[0]]()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation based on an instance of a class"""
        if not arg:
            print("** Class name missing **")
            return True

        arg_split = arg.split(" ")
        if len(arg_split) > 0:
            if arg_split[0] not in ShopNestCommand.classes:
                print("class name does not exist")
            else:
                if len(arg_split) == 1:
                    print('I am a good man')





if __name__ == '__main__':
    ShopNestCommand().cmdloop()
    
 