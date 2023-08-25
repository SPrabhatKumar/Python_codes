class Maths:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The square of {self.number} is: {self.number**2}")
    def sqaureroot(self):
        print(f"The square root of {self.number}is :{self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is :{self.number**3}")
    @staticmethod
    def greet():
        print("Thank you !Your work is Done ")
n=int(input("Enter a number :"))
value=Maths(n)
value.square()
value.sqaureroot()
value.cube()
value.greet()

