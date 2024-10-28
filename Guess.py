secret_number=9
guess_count=0
guess_limit=3
user=input("User name:")
while guess_count < guess_limit:
    guess=int(input("Guess : "))
    guess_count +=1
    if guess == secret_number:
        print(f"{user} Won The Game!!!")
        break
else:
    print(f"{user} Loss The Game ")