import engine,os

class Preferences:
    def __init__(self):
        self.config_dir = "config"
        self.data = dict()
        self.index = 0
        
        self.load_config()
        
    def __getitem__(self,key):
        return self.data[key]
    
    def load_config(self):
        cfg = open(self.config_dir)
        for l in cfg:
            i = l.split(" ")
            self.data[i[0]] = i[1]
        self.index = len(self.data)
