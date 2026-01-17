#!/usr/bin/env python

import cmd


class ShopNestCommand(cmd.Cmd):
    prompt = '(shopnest) '

    def do_quit(self, arg):
        """Cammand that quites the command line"""

        print('Quiting the command line ...')
        return True

    def do_EOF(self, arg):
        """Exits the interpreter"""

        print('n\Exiting the CLI...')
        return True

    def emptyline(self, arg):
        """Do nothing when an empty line is ecountered"""

        pass

    def default(self, arg):
        """Handles invalid commands"""

        print(f'Error: {arg} is an invalid command, Type "Help" to sse available commands')


if __name__ == '__main__':
    ShopNestCommand().cmdloop()