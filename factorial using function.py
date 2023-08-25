def factorial_iter(n):
    product=1
    for i in range(n):
        product=product *(i+1)
    return product
b=int(input("Enter the number :\n"))
a=factorial_iter(b)
print(f"The factorial  is :{a}")