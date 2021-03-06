# system
import argparse

# local
from ._constants import COMMAND_HELP_TEXT_NAME, KIWI_HELP_TEXT_NAME


class Parser:
    """Singleton: Main CLI arguments parser"""

    class __Parser:
        """Singleton type"""

        # argparse objects
        __parser = None
        __subparsers = None
        __args = None

        def __init__(self):
            # add version data from separate file (keeps default config cleaner)
            with open(KIWI_HELP_TEXT_NAME, 'r') as stream:
                kiwi_help = stream.read()

            with open(COMMAND_HELP_TEXT_NAME, 'r') as stream:
                command_help_text = stream.read()

            # create main parser
            self.__parser = argparse.ArgumentParser(
                prog='kiwi',
                description=kiwi_help,
                epilog=command_help_text,
            )
            self.__parser.formatter_class = argparse.RawDescriptionHelpFormatter

            # main arguments
            self.__parser.add_argument(
                '-v', '--verbosity',
                action='count', default=0
            )

            # attach subparsers
            self.__subparsers = self.__parser.add_subparsers()
            self.__subparsers.required = True
            self.__subparsers.dest = 'command'

        def get_subparsers(self):
            return self.__subparsers

        def get_args(self):
            if self.__args is None:
                # parse args if needed
                self.__args, unknowns = self.__parser.parse_known_args()
                self.__args.unknowns = unknowns

            return self.__args

    __instance = None

    def __init__(self):
        if Parser.__instance is None:
            # create singleton
            Parser.__instance = Parser.__Parser()

    def __getattr__(self, item):
        """Inner singleton direct access"""
        return getattr(self.__instance, item)
