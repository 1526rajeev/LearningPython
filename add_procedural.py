#step1  get the first number
print("enter first input")
x = input()
print("first value is " + x)
print("enter second input")
y = input()
print("second value is " + y)
# ADD the numbers and store the result
print("result")
z = (int(x) + int(y))
if z < 0:
    print(abs(z))
else:
    print(z)
