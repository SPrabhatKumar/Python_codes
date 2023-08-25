class Employee:
    company="google"
    def printinfo(self):
        print(f"The employee working in {self.company} \nSalary is :{self.salary}")
    @staticmethod #it is used when you want to not pass the arguement self
    def greet():
        print("Good Work folks!")
prabhat=Employee()
prabhat.salary=1000
prabhat.printinfo()#it is similar as Employee.printinfo(prabhat)
prabhat.greet()