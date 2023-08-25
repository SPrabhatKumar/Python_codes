class Employee:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getinfo(self):
        print(f"The Name of comapny is :{self.company}\nThe Name of Employee is :{self.name}\nThe Poduct is :{self.product}")
prabhat=Employee("Prabhat","skype")
prince=Employee("Prince","Github")
prabhat.getinfo()
prince.getinfo()
