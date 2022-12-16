from configparser import ConfigParser

config = ConfigParser()


def get_data_from_file(section=None, key=None):

    if section == None or key == None:
        return 'Parameters are not given.'

    else:
        config.read("../src/configs/config.ini")
        text = config.get(section, key)

        return text

