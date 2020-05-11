print("Welcome to guess the number game.")
import random
number = random.randint(0,20)

print("I'm guessing number from 0 to 20.....! ")
print("What do you think it would be :)")

for c in range(21):
    if c ==4:
        print("Your chances are over , you lost , the number was: ",number)
        break
    guess = int(input("What's the number: "))
    if guess == number:
        print("Yes this is the number. You guessed it in ", c+1,"attempts")
        break

    elif guess > number :
        print("Too much high")

    elif guess < number :
        print("Too much low")

    else:
        print("unexpected behavior")

