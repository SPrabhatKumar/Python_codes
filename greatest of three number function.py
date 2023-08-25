def greatest(a,b,c):
    if a>b:
        p=a
    else:
        p=b
    if b>c:
        p1=b
    else:
        p1=c
    if p>p1:
        print( "the greater number is"+str(p))
    else:
        print("the greater number is ",str(p1) )
d=greatest(4,8,6)
print(d) 