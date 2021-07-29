import json
from sys import path

class loadAccount:
    def __init__(self) -> None:
        pass

    def load(self, accountName):
        path = "./mdp/" + accountName + ".json"

        file = open(path, "r")
        data = json.loads(file.read())
        
        print(data)