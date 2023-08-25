from functools import reduce
sum=lambda a,b:a+b
list1=[4,24,56,32,6]
val=reduce(sum,list1)
print(val)
print(reduce(sum,list1))