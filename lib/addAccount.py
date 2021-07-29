import json

class addAccount:
    def __init__(self) -> None:
        pass
    
    def add(self, typeName):
        path = "./mdp/" + typeName + ".json"

        login = input("youre accont login please..")
        mdp = input ("youre accont mdp please..")

        print("loding ..")

        data = {
            "login": login,
            "mdp": mdp
        }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file)
