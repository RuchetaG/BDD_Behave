from configparser import ConfigParser


def login_data_reader(section, key):
    config = ConfigParser()
    config.read(r'./ConfigurationFiles/Config.cfg')
    return config.get(section, key)


def config_reader(section, key):
    config = ConfigParser()
    config.read(r'./ConfigurationFiles/Config.cfg')
    return config.get(section, key)


def elements_reader(section, key):
    config = ConfigParser()
    config.read(r'./ConfigurationFiles/elements.cfg')
    return config.get(section, key)


