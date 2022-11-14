## using for loop to get even numbers
x = int(input("enter first number"))
y = int(input("how many odd numbers you wish to print?"))
cc = 0
if x%2==0:
    num=x+2
else:
    num=x+1
    cc=0
for odd in range (cc,y,1):
    print(num)
    num=num+2
