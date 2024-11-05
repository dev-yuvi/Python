def division(num,div):
    try:
        result=num/div
        return result
    except ZeroDivisionError:
        return "zero can't divisable"




try:
    num=int(input("Enter Number: "))
    div=int(input("Enter The Divicer: "))
    print(division(num,div))
except ValueError:
    print("Numbers only valid!!!")