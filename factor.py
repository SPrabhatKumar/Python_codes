import string
a=int(input('Enter a number :'))
factor=[]
for i in range(1,a+1):
    if a%i==0:
        factor.append(i)
print(f"The factor of {a} is :".format(a))
# factor=factor.join()
print(factor)
