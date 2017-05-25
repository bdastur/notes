#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Command Pattern
'''

import os


class CreateFile(object):
    def __init__(self, filepath, name, data=None):
        self.filepath = filepath
        self.name = name
        self.data = data

    def execute(self):
        if os.path.exists(self.filepath):
            print "File already exists"
            return

        with open(self.filepath, 'w') as fhandle:
            if self.data is not None:
                fhandle.write(self.data)


class DeleteFile(object):
    def __init__(self, filepath, name):
        self.filepath = filepath
        self.name = name

    def execute(self):
        if os.path.isdir(self.filepath):
            print "Directory"
            os.rmdir(self.filepath)
        else:
            os.remove(self.filepath)


class Invoker(object):
    '''
    This invoker class adds another layer of abstraction to the
    clients. It could be useful in cases to keep track of commands
    executed, or the invoker could implement batching, sequencing,
    async operations etc.
    '''
    def __init__(self):
        self.commands = []
        self.history = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for cmd in self.commands:
            execute_method = getattr(cmd, 'execute', None)
            if callable(execute_method):
                cmd.execute()
                self.history.append("Oper: " + cmd.name)
            else:
                print "Command does not have execute method"

    def print_history(self):
        for history in self.history:
            print history


def main():
    commands = []
    newfile = "/tmp/testfile.txt"

    commands.append(CreateFile(newfile, "create file"))
    commands.append(DeleteFile(newfile, "delete file"))

    for command in commands:
        command.execute()

    # Using an invoker.
    print "Using invoker"
    invoker = Invoker()
    invoker.add_command(CreateFile(newfile, "create file"))
    invoker.add_command(DeleteFile(newfile, "delete file"))

    invoker.execute_commands()

    invoker.print_history()



if __name__ == '__main__':
    main()
