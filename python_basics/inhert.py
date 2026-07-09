class Baseclass:
    def __init__(self):
        pass

    def printName(self, sName):
        print("Hello",sName)

class ChildClass(Baseclass):
    def __init__(self):
        super().__init__()

    def CallFromChild(self,inputName):
        self.printName(inputName)



cls=ChildClass()
cls.CallFromChild("Garima")

