words=["mote","kadu","bastard",'bad',"dog"]

with open("replace.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"good boy")
with open("replace.txt",'w') as f:
    f.write(content)
