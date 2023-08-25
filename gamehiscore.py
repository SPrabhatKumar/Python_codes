def game():
    return (800)
with open("hiscore.txt") as f:
    string=f.read()
if string=="":
    with open("hiscore.txt",'w') as f:
        f.write(str(game()))
elif int(string)<game():
    with open ("hiscore.txt","w") as f:
        f.write(str(game()))