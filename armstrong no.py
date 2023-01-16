def armstrong():
    n=int(input("enter no to be checked"))
    a=n
    p=""
    while n>0:
        s=n%10
        p=p+str(s)
        n=n//10 
 
    if eval(p)==a:
        return True
    else:
        return False
f=armstrong()
if f==True:
    print("no is armstrong")
else:
    print("not armstrong") 
 
 
