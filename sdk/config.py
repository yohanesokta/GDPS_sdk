import json
import os

filename = "./gdpsconfig.json"

def createDefaultConfig():
    data_default = {
        "ignore" : [
        ]
    }
    with open(filename,"w") as file:
        json.dump(data_default,file,indent=4)

def writeConfig(config):
    with open(filename,"w") as file:
        json.dump(config,file,indent=4)

def readConfig():
    if (not os.path.exists(filename)):
        createDefaultConfig()
    file = open(filename)
    data = json.load(file)
    file.close()
    return data

class Config:
    def __init__(self):
        self.data = readConfig()
    
    def all(self):
        return self.data
    
    def stagging(self):
        return self.data.get("stagging")
    
    def update_stagging(self,filename):
        if (self.data.get("stagging")):
            self.data["stagging"].append(filename)
            writeConfig(self.data)
        else:
            self.data["stagging"] = [filename]
            writeConfig(self.data)

    def ignore(self):
        return(self.data.get("ignore"))

config = Config()