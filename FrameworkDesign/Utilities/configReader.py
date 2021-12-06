import json
from configparser import ConfigParser

import pytest


def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\configuration\\config.ini")
    return config.get(section, key)





def config(self):
    # Read the file
    with open("..\\configuration\\config.json") as config_file:
        config = json.load(config_file)
        return config

    # # Assert values are acceptable
    # assert config['browserName'] in ['Firefox', 'Chrome', 'Headless Chrome']
    # assert isinstance(config['implicit_wait'], int)
    # assert config['implicit_wait'] > 0

    # Return config so it can be used





