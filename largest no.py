#Q9.WAP in python to find largest of three numbers
a=int(input("Enter any no"))
b=int(input("Enter any no"))
c=int(input("Enter any no"))
if (a>b and a>c):
    print(a,"is greatest")
elif(b>a and b>c):
    print(b,"is greatest")  
else:
    print(c,"is greatest")
