class Railway:
    formtype="RAILWAYFORM"
    def printinfo(self):
        print(f"The Passenger Name is :{self.name}")
        print(f"The Train is:{self.train}")

prabhat=Railway()
prabhat.name="Prabhat kumar singh"
prabhat.train="RajdhaniEXpress"
prabhat.printinfo()