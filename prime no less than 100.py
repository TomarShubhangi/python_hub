#Q12. WAP to print prime no less than 100?
for a in range(1,101):
    count=0
    for i in range(2,(a//2+1)):
        if(a%i==0):
            count+=1
            break
    if(count==0 and a!=1):
        print(" %d" %a,end="")
    