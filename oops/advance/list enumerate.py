list=[2,35,66,7,89,43,234,42]
for index,item in enumerate(list):
    if index==2 or index==4 or index==6:
        print(f"The {index+1} Element in List is:{item}")
        # print(item)