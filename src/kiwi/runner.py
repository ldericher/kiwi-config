# system
import logging

# local
from .config import LoadedConfig
from .parser import Parser
from .subcommands import *

###########
# CONSTANTS

# all available subcommands
SUBCOMMANDS = [
    InitCommand,
    ShowCommand,
    LogsCommand,
    CmdCommand,
    ShellCommand
]


class Runner:
    """Singleton: Subcommands setup and run"""

    class __Runner:
        """Singleton type"""

        __parser = None
        __commands = []

        def __init__(self):
            # setup all subcommands
            for cmd in SUBCOMMANDS:
                self.__commands.append(cmd())

        def run(self):
            """run the desired subcommand"""

            args = Parser().get_args()

            for cmd in self.__commands:
                if str(cmd) == args.command:
                    # command found
                    logging.debug(f"Running '{cmd}' with args: {args}")
                    cmd.run(LoadedConfig.get(), args)
                    return True

            # command not found
            logging.error(f"kiwi command '{args.command}' unknown")
            return False

    __instance = None

    def __init__(self):
        if Runner.__instance is None:
            # create singleton
            Runner.__instance = Runner.__Runner()

    def __getattr__(self, item):
        """Inner singleton direct access"""

        return getattr(self.__instance, item)
