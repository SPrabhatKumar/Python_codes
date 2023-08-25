class Employee:
    company="Google"
prabhat=Employee()
saiteja=Employee()
print(prabhat.company)
print(saiteja.company)
Employee.company="You Tube"
print(prabhat.company)
print(saiteja.company)