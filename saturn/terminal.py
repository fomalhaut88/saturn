"""
Terminal implements a command line where you can rerun a module and manage
the scope.
"""

import os
import sys
import readline
import traceback
from importlib import reload

from .version import __version__
from .scope import Scope


class Terminal:
    welcome = "Welcome to Saturn terminal where you can reruns " \
              "your Python module keeping its scope in RAM. " \
              "Version {}.".format(__version__)
    prompt = "S>>> "

    def __init__(self):
        # Dictionaly to store imported modules
        self._modules = {}

    def run(self):
        # Define empty scope
        scope = Scope()

        # Print welcome
        print(self.welcome)

        # Terminal loop
        while True:
            # Wait for a command
            command = input(self.prompt).strip()

            # Skip if the command is empty
            if not command:
                continue

            # Exit
            elif command == "exit":
                break

            # Run module
            elif command.startswith("run "):
                module_name = command[4:]
                self._run_module(module_name, scope)

            # Execute a python expression
            else:
                try:
                    exec(command, {'scope': scope})
                except BaseException:
                    traceback.print_exc()

    def _run_module(self, module_name, scope):
        # Catch all exceptions (including syntax and keyboard interruptions)
        try:
            # Import or reload the module
            if module_name not in self._modules:
                self._modules[module_name] = __import__(module_name)
            else:
                reload(self._modules[module_name])

            # Get target to run
            target = __import__('saturn').target

            # Run with the scope
            target(scope)

        except BaseException:
            traceback.print_exc()


def main():
    # Add path of the run script to sys.path
    sys.path.append(os.getcwd())

    # Create and run terminal
    terminal = Terminal()
    terminal.run()
