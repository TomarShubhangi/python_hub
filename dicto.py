#Q8.WAP in python to demonstrate working with dictonaries
classXI=dict()
n=int(input("enter  no of section"))
i=1
while i<=n:
  a=input("enter section")
  b=input("enter stream")
  classXI[a]=b
  i+=1
print("class",'\t',"section",'\t',"stream")
for i in classXI:
  print("XI",'\t',i,'\t',classXI[i])
  