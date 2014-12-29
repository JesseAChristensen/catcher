import ConfigParser
import os
import getopt
import catcher

def main(argv):
    config = []
    try:
        opts, args = getopt.getopt(argv, "hc:", ["config="])
    except getopt.GetoptError:
        print('syntax is catcher.py -c "/path/to/catcher.conf"')
        print('otherwise catcher.py will look for .catcher.conf')
        print("in the user's home directory")
    for opt, arg in opts:
        if opt == "-h":
            print('syntax is catcher.py -c "/path/to/catcher.conf"')
            print('otherwise catcher.py will look for .catcher.conf')
            print("in the user's home directory")
            sys.exit()
        elif opt in ("-c", "--config"):
            config.append(arg)
    return(config)

def parseConfig(confs):
    for item in confs:



config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.catcher.conf')
