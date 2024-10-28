row=int(input())
col=int(input())
matrix=[]
for r in range (row):
    m=[]
    for  c in range (col):
        m.append(int(input()))
    matrix.append(m)
print(matrix)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()