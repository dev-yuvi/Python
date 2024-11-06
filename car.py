started=False
while True:
    commend=input("> ").lower()
    if commend == "start":
        if started == True:
            print("Car is already started !")
        else:
            started=True
            print("Car is started !")
    elif commend == "stop":
        if started == False:
            print("Car is already stopped !")
        else:
            started=True
            print("Car is stopped")
    elif commend =="help":
        print("""
start -> to start the car
stop -> to stop the car
quite -> to quite the game
""")
    elif commend =="quit":
        break
    else:
        print("I don't understand !!!")