#Q20.WAP in python to print transpose of a matrix?
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
print("Enter the elements of Matrix:")
matrix = []
for i in range(r):
    matrix.append([])
    for j in range(c):
        val = int(input())
        matrix[i].append(val)
print("Matrix is: ")        
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()

temp = []
for i in range(r):
    for j in range(c):
        temp[i][j]= matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp[i][j]
print("The Transpose is : ")
for i in range(c):
    for j in range(r):
        print(matrix[i][j], end=" ")
    print()
    
