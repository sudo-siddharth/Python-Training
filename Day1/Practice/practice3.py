x = "hello"

def myfun():
    global x
    x="some"

myfun()

print(x)