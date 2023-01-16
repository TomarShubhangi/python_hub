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
for n in matrix:
    print (n)
transpose = [[matrix[j][i] for j in range (len (matrix))] for i in range (len (matrix[0]))]
print("Transpose is: ")        
for r in transpose:
    print (r)

