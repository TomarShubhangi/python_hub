#Q18.WAP to convert integer to binary?
def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n%2,end='')

# Driver code
if __name__ == "__main__":
    dec=int(input("Enter no: "))   
    print("No in Binary format is: ",end = " ")
    convertToBinary(dec)
