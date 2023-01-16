n = int(input("Enter no :"))
for k in range(0, n):
    for m in range(n-1, k-1):
        print("*", end="")
    for j in range(k):
        print(' ', end="")
    for h in range(k + 1, n+1):
        print("*", end="")
    print( )
    
