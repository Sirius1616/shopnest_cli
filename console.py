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
                if len(arg_split) < 2:
                    param = arg_split[2:].split(' ')
                    dict_param = {}
                    for params in param:
                        key, value = params.split('=')
                        dict_param[key] = value
                    print(dict_param)
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
                    print('** instance id missing **')
                else:
                    new_obj = storage.all()
                    obj_id = '.'.join([arg_split[0], arg_split[1]])
                    if obj_id in new_obj:
                        print(new_obj[obj_id])
                    else:
                        print("** no instance found **")

                        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** Class name missing **")
            return True

        arg_split = arg.split(" ")
        if len(arg_split) > 0:
            if arg_split[0] not in ShopNestCommand.classes:
                print("class name does not exist")
            else:
                if len(arg_split) == 1:
                    print('** instance id missing **')
                else:
                    new_obj = storage.all()
                    obj_id = '.'.join([arg_split[0], arg_split[1]])
                    if obj_id in new_obj:
                        del new_obj[obj_id]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""

        arg_split = arg.split(" ")
        
        new_dict = {}
        load_obj = storage.all()
        if not arg:
            for key, value in load_obj.items():
                new_dict[key] = value.to_dict()
            print(new_dict)
        else:
            count = 0
            for key, value in load_obj.items():
                class_name = key.split('.')[0]
                if class_name == arg_split[0]:
                    new_dict[key] = value.to_dict()
                    count += 1
            if count == 0:
                print("** class doesn't exist **")
            else:
                print(new_dict)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** Class name missing **")
            return True

        arg_split = arg.split(" ")
        if len(arg_split) > 0:
            if arg_split[0] not in ShopNestCommand.classes:
                print("class name does not exist")
            else:
                if len(arg_split) < 2:
                    print('** instance id missing **')
                else:
                    new_obj = storage.all()
                    obj_id = '.'.join([arg_split[0], arg_split[1]])
                    if obj_id in new_obj:
                        if len(arg_split) > 2:
                            if len(arg_split) > 3:
                                setattr(new_obj[obj_id], arg_split[2], arg_split[3])
                                storage.save()
                            else:
                                print('** value missing **')
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')





if __name__ == '__main__':
    ShopNestCommand().cmdloop()
    
 