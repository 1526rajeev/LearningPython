#find out the slice of that string after removing first and last character
x=input("what is string")
#find out the slice of the  string removing first and last character
y=len(x)
x1=x[1: -1]
print(x1)
#find out the slice of the string after removing the first 2 characters

x2=x[2:]
print(x2)
 #find out the slice of the string after removing the last 2 characters

x3=x[:-2]
print(x3)

#slice the string in the middle and display both strings

x4=x[int(len(x)/2)]
print(x,x4)

