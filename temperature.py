#Q11. WAP to convert temperature from C to F & reverse
temp=input("input temp in C or F: ")
deg=int(temp[:-1])
a=temp[-1]
if a.upper()=="C":
    result=int(round((9*deg)/5+32))
    b="FARENHEIT"
elif a.upper()=="F":
    result=int(round((deg-32)*5/9))
    b="CELCIUS"
else:
    print("Input proper convention")
    quit()
print("temperature in",b,"is",result,"deg")
