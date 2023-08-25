import random
set1=[]
for i in range(20):
    rand=random.randint(1,20)
    set1.append(rand)
print(set1)
set2=[]
for i in set1:
    if i not in set2:
        set2.append(i)
print("After Removal of same elements from list:",set2)
set2.sort()
print("The sorted list is:",set2)