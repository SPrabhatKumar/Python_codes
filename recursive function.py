def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
a=int(input("Enter the number :"))
p=sum(a)
print("The sum first "+str(a)+"number is: "+str(p))