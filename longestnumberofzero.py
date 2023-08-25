import random
set=[]
count=0
for i in range(100):
    rand=random.randint(0,1)
    set.append(rand)
print("The list is:",set)
temp=0
for i in set:
    if i==0:
        temp=temp+1
    else:
        if temp>count:
            count=temp
        temp=0
print("The longest run of zero is",count)