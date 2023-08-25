with open (".txt")as f:
    content =f.read()
content=content.replace("prabhat","twinkle")
with open(".txt","w") as f:
    f.write(content)