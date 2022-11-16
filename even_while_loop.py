#print even numbers using while loop
x = int(input("enter first number"))
y = int(input("how many even numbers you wish to print?"))
if x%2==0:
    #print(x+1)
    num=x+2
else:
    #print(x+2)
    num=x+1

count= 0
while count<y:
    print(num)
    count=count +1
    num= num+2
