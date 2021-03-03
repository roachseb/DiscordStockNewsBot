#Load Configs
import configparser


class Configs():
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.path = ".config"
        self.parser.read(self.path)
        self.sections = self.parser.sections()
        dict2 = {}
        for k in self.sections:
            dict1 = {}
            options = self.parser.options(k)
            for option in options:
                try:
                    dict1[option] = self.parser.get(k, option)
                    if dict1[option] == -1:
                        DebugPrint("skip: %s" % option)
                except:
                    print("exception on %s!" % option)
                    dict1[option] = None
            dict2.update(dict1)
        for k,v in dict2.items():
            setattr(self,k,v)
