print(''' 1: area of triangle 2: area of square 3: area of rectangle''')
choice= int(input("enter choice"))
def triangle():
    n=int(input("enter base of triangle"))
    p=int(input("enter height of triangle"))
    print("area of triangle =",(n*p)/2)
def square():
    n=int(input("enter side of square"))
    print("area of square=",n**2)
def rectangle():
    n=int(input("enter length of rectangle"))
    b=int(input("enter breadth of rectangle"))
    print("area of rectangle=",n*b)
if choice==1:
    triangle()
elif choice==2:
    square()
elif choice==3:
    rectangle()
