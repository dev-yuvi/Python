n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==n-1+i or j==n-i+1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()