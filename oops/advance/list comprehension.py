list1=[33,6,7,8,9,4,353,234,243]
# b=[]
# for item in list1:
#     if item%2==0:
#         b.append(item)
# print(b)
# this can be done by list comprehension 
b=[i for i in list1 if i%2==0]
print(b)
set={i for i in list1}
print(set)