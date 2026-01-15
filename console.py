#!/usr/bin/env python

import cmd


class ShopNestCommand(cmd.Cmd):
    prompt = '(shopnest)'

    def do_quit(self, arg):
        """Cammand that quites the command line"""

        print('Quiting the command line ...')
        return True

    def do_EOF(self, arg):
        """Exits the interpreter"""

        print('n\Exiting the CLI...')