num=int(input("Enter a number :"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
if prime:
    print("The Number is Prime Number")
else:
    print('The Number is not prime number ')