len=int(input("Enter The Length: "))
matrix=[]
for i in range(len):
    matrix.append(int(input()))

unique=[]
for number in matrix:
    if number not in unique:
        unique.append(number)
print(unique)