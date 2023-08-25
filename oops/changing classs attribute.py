class Employee:
    company="google"
prabhat=Employee()
prince=Employee()
print(prabhat.company)
print(prince.company)
Employee.company="you tube"
print(prince.company)
print(prabhat.company)