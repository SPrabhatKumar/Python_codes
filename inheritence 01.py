class Employee:#parent class or base class 
    company="google"
    def showDetails(self):#child class or derived class 
        print(f"The company is {self.company}")
class Programer(Employee):
    language="python"
    def getinfo(self):
        print(f"The language is {self.language}")
prabhat=Programer()#can be accessed both the element of parent and child class 
print(prabhat.company)
prabhat.showDetails()
prabhat.getinfo()