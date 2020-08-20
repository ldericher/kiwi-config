# system
import logging
import os

# local
from ._constants import KIWI_CONF_NAME
from .config import LoadedConfig
from .projects import Projects


class Instance:
    __directory = None
    __config = None
    __projects = None

    def __init__(self, directory='.'):
        if not os.path.isdir(directory):
            logging.warning(f"Invalid directory in instance creation: '{directory}'")
            directory = os.getcwd()

        self.__directory = os.path.abspath(directory)
        self.__config = LoadedConfig.get(directory)
        self.__projects = Projects.from_dir(directory)

    def exists(self):
        return os.path.isfile(os.path.join(self.__directory, KIWI_CONF_NAME))
