"""Q14.WAP in python that accepts length of a triangle as input, the 
program should indicate whether or not the tringle is right angled &
calculate Area & Permeter of it?""" 
def right_angled(a, b, c):
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        return "The triangle is right-angled." 
    else:
        return "The triangle is not right-angled."

#Driver code
if __name__ == "__main__":
    a=float(input("Enter base side : "))
    b=float(input("Enter second side : "))
    c=float(input("Enter third side : "))
    s=(a+b+c)/2  
    Area=(s*(s-a)*(s-b)*(s-c))**0.5
    peri=a+b+c
    print("Right angled tringle or not:",right_angled(a, b, c))
    print("Area of the triangle is %0.2f" %Area)
    print("Perimeter of triangle:",peri)