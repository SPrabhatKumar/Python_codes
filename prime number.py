num=int(input("Enter the number :\n"))
f=True
for i in range(2,num):
    if num%i==0:
        f=False
        break
if f:
    print(" This is  prime number ")
else:
    print(" This is not prime number ")
