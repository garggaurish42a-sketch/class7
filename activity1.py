x=20
if(type(x) is int):
    print("true")
else:
    print("false")
y=20.7
if(type(y) is not float):
    print("true")
else:
    print("false")
x=20
y=20
if x is y:
    print("x and y are of same identity")
y=30.9
if x is not y:
    print("x and y are of different identity")