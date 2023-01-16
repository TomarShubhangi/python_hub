#Q7.WAP in python to demonstrate working with tupples
t1=tuple()
t2=tuple()
n=int(input("enter no of values"))
i=0
while i<n:
  a=input("Enter value")
  t1+=(a,)
  b=input("Enter value")
  t2+=(b,)
  i+=1
print(t1)
print(t2)
t1,t2=t2,t1
print("swapped tuple:")
print(t1)
print(t2)
