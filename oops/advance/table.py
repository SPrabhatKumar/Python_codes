num=int(input("Enter a number :"))
list=[num*i for i in range(1,11)]
with open("table.txt","a")as f:
    f.write(str(list))
    f.write("\n")
