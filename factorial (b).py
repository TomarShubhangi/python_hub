#Q13. WAP to find factorial of a no using-A:function, B:Recursion ?
num=int(input("Enter no: "))
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
result=factorial(num)
print("The factorial of",num,"is",result) 
