print("first input")
x = input()
if int(x)<0:
    print("na")
    exit()
else:
    print("first number is "+ x)

    print("second input")
    y = input()
    if int(y)<0:
        print("na")
        exit()
    else:
        print("second number"+ y)
        expon= int(x)**int(y)
        print("results")

        print(expon)