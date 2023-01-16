#Q10. WAP to impliment simple calculator
print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Quotient \n 5.Remainder")
a= int(input("enter 1 no:"))
b= int(input("enter 2 no:"))
choice= int(input("enter choice"))
if choice==1:
    print("Addition:",a+b)
elif choice==2:
    print("Subtraction:",a-b)
elif choice==3:
    print("Multiplication:",a*b)
elif choice==4:
    print("Quotient:",a/b)
elif choice==5:    
    print("Remainder:",a%b)
else:
    print("INVALID CHOICE")    