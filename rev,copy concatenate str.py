#Q17.WAP in python to reverse, copy & concatenate a string?
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s=input("Enter string:")
print("The original string is : ", end="")
print(s)
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
#copy a string
str1=input("Please new String : ")
str2=''
for i in str1:
    str2 = str2 + i
print("The Final copied String : Str2  = ", str2)
#cocatenate a string
str2=input("Enter next string : ")
str3=str1+str2
print("concatenation of string : ",str3)