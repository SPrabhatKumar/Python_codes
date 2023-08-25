expression=input("Enter the expression:")
a=[]
n=len(expression)
for i in range(n-1):
    a.append(expression[i])
    if expression[i+1].isalpha() or expression[i+1]=='(':
        a.append('*')
a.append(expression[n-1])
ans="".join(a)
print(ans)
