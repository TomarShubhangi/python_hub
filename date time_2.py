#Q5.WAP to print current date & time in 
#"Sun May 20 02:26:23 IST 2019"
from datetime import datetime
now=datetime.now()
nmt=now.strftime("%a %b %d %H:%M:%S IST %Y")
print(nmt)
