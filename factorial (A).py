#Q13. WAP to find factorial of a no using-A:function, B:Recursion ?
n=int(input("Enter no:" ))
fact=1
if n<0:
    print("sorry,Factorial does not exists")
elif n==0:
    print("Factorial of the no is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial of the given no is:", fact)  
        