import random
a=[]
for i in range (20):
    x=random.randint(1,100)
    a.append(x)
print(a)
print(f"The average of List elements is:{sum(a)/len(a)}")
print(f"The max value is :{max(a)}")
print(f"The minium value in the list is:{min(a)}")
a.sort()
print("the sorted list is :",a)
print(f'The second largest number in the list is :{a[18]}')
print(f'The second smallest number in the list is :{a[1]}')
count=0
for i in a:
    if i%2==0:
        count=count+1
print("The number of even number in the list is :",count)
