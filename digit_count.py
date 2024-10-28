num=[12,34,56,78,90]
rev=[]
for element in  num:
    sum=0
    for digit in str(element):
        sum+=int(digit)
    rev.append(sum)
print(str(rev))