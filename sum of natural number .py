def sum(num):
    if num==1:
        return 1
    else:
        return sum(num-1)+num
a=int(input("Enter the number: "))
b=sum(a)
print(f"The sum of {a} natural number is {b}")