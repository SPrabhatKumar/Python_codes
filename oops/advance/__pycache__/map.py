def square(x):
    return x*x
# square=lambda x:x*x can be also
list1=[2,34,55,8,4]
# Method 1
l2=[]
for item in list1:
    l2.append(square(item))
print(l2)
# Method 2
# l2=list(map(square,list1))----->this both are same
# print(l2)                 ---->this both are similar as below
print(list(map(square,list1)))
# filter method
# def greaterthan5(num):
#     if num>6:
#         return True
#     else:
#         return False
greaterthan5=lambda num:num>5
print(list(filter(greaterthan5,list1)))
