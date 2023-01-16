#Q5.WAP to print current date & time in the following format:
#"Sun May 20 02:26:23 IST 2019"
from datetime import datetime
now=datetime.now()
week=now.strftime("%a")
month=now.strftime("%b")
day=now.strftime("%d")
time=now.strftime("%H:%M:%S")
year=now.strftime("%Y")
print(week,month,day,time,"IST",year)
