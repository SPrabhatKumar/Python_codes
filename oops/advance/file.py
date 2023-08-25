def readfile(filename):
    try:
        with open(filename,"r")as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")
readfile("one.txt")
readfile("two.txt")
readfile("three.txt")