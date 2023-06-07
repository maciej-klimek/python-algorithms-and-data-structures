
try:
    print(x)
except:
    print("NameError exception")

try:
    x = 10
    x = x/0
except:
    print("ZeroDivisionError exception")

try:
    tbl = [1, 2, 3]
    print(tbl[3])
except:
    print("IndexError exception")