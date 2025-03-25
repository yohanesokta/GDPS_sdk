import json
import os

filename = "./gpsconfig.json"

def createDefaultConfig():
    data_default = {
        "ignore" : [
        ]
    }
    with open("gpsconfig.json","w") as file:
        json.dump(data_default,file,indent=4)

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
    def ignore(self):
        return(self.data.get("ignore"))
    

config = Config()