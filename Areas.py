n=int(input("Enter no like: 1.area of rect , 2.area of triangle, 3. area of square"))
if n==1:
  l=int(input("enter length"))
  b=int(input("enter breadth"))
  area=l*b
  print("rect",area)
elif n==2:
  b=int(input("enter base"))
  h=int(input("enter height"))
  area=1/2*b*h
  print("trig",area)
elif n==3:
  l=int(input("enter length"))
  area=l*l
  print("square",area)
else:
  print("the choice is not avail")
  
  
  
