class PartyAnimal:
    def __init__(self):
        self.x=0
        
    
    def party(self,nameval):
        self.x=self.x+1
        self.name=nameval
        print("total members:", self.x,": Member Name ", self.name)

    def __del__(self):
        print("Deleting self")

class NewParty(PartyAnimal):
    def __init__(self):
        super().__init__()

    def touchdown(self,sportName):
        print("in touchdown method")
        self.party(sportName)
        print("out of touchdown method")


an=NewParty()
an.touchdown("Cricket")
#an=PartyAnimal()
##an.party("Varun")
#an.party("Garima")
#an.party("Anshu")



