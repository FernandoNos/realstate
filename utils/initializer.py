import ConfigParser

FILE = "real_state_config.cfg"
def getURL():
	Config = ConfigParser.ConfigParser()
	Config.read(FILE)
	return Config.get("Configuration", "URL")


def getKey():
	Config = ConfigParser.ConfigParser()
	Config.read(FILE)
	return Config.get("Configuration", "KEY")