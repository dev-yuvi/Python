weight=int(input("Enter The Weigth:"))
print("Type (L) are (Kg)")
str=input()
if str.upper() == 'L':
    print(weight*0.45)
elif str.upper() == 'K':
    print(weight/0.45)
else:
    print("Sorry")
