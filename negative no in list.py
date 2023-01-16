#Q22.WAP in python to Print all negative no in a list?
list=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    list.append(b)
for num in list:
    if num < 0:
        print(num, end=" ")

