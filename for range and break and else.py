# 1.it prints 1 to 7 starting from 0
for i in range(8):
    print(i)
# 2.it prints 2 to 7 
for i in range(2,8):
    print(i)
# 3.its print 1 to 7 with skip value 1
for i in range(1,8,2):
    print(i)
# 4.for else loop with break 
# 4(a) else part will be executed 
for i in range(1,8,2):
    print(i)
else:
    print("Done")
# 4(b) else part will be not executed
for i in range(1,8):
    print(i)
    if i==5:
        break

else:
    print("Done")