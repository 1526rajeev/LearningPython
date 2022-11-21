# subtraction function

def subt(x, y):
    z = int(x)-int(y)
    print(z)

x1 = input("enter first value: ")
if int(x1) <0:
    print("please enter a positive value")
    exit()
y1 = input("enter second value: ")
if int(y1) <0:
    print("please enter a positive value")
    exit()
subt(x1,y1)


