number=input("EnterThe Number: ")
digits={
    "0":"Zero",
    "1":"One",
    "2":"Tow",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for ch in number:
    output+=digits[ch]+" "
print(output)