# calculator
# 1 ADD two numbers
def add(X,Y):
    return x+y

# 2 SUB two numbers
def sub(x,y):
    return x-y

#3 MUL two numbers
def mul(x,y):
    return x*y
#4 def div two numbers
def div(x,y):
  return x/y

#5 Remainder
def rem(x,y):
    return x%y

#6 quotient
def quo(x,y):
    return x//y

#7 expo
def exp(x,y):
    return x**y

print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.rem")
print("6.quo")
print("7.exp")

while True:
    #take input from the user
    option = input("enter option(1/2/3/4/5/6/7):")

if option in ('1', '2', '3', '4','5','6', '7'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option== '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif option == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif option == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    if option == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif option == '5':
        print(num1, "%", num2, "=", remainder(num1, num2))

    elif option == '6':
        print(num1, "//", num2, "=", quotient(num1, num2))

    elif option == '7':
        print(num1, "**", num2, "=", expo(num1, num2))

# calculator
# 1 ADD two numbers
def add(X,Y):
    return x+y

# 2 SUB two numbers
def sub(x,y):
    return x-y

#3 MUL two numbers
def mul(x,y):
    return x*y
#4 def div two numbers
def div(x,y):
  return x/y

#5 Remainder
def rem(x,y):
    return x%y

#6 quotient
def quo(x,y):
    return x//y

#7 expo
def exp(x,y):
    return x**y

print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.rem")
print("6.quo")
print("7.exp")

while True:
    #take input from the user
    option = input("enter option(1/2/3/4/5/6/7):")

if option in ('1', '2', '3', '4','5','6', '7'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option== '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif option == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif option == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    if option == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif option == '5':
        print(num1, "%", num2, "=", remainder(num1, num2))

    elif option == '6':
        print(num1, "//", num2, "=", quotient(num1, num2))

    elif option == '7':
        print(num1, "**", num2, "=", expo(num1, num2))


  #check if user wants another calculation
    #break the while loop if answer is no
    next_calculation == input("let's do next calculation?(yes/no):")
    if next_calculation== "no":
        break

