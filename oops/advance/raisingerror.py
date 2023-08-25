def increment(num):
    try:
        return num+1
    except:
        raise ValueError("Pls enter valid code")
a=increment('ds')
print(a)