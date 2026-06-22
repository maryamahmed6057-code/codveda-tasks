import random
secret_number=random.randint(1,100)

attempts= 4
print("-------------------- welcome to number guessing game----------------")
print("guess number between 1 and 100")
print ("you have", attempts ,"attempts")

while attempts >0:
    guess= int((input("enter your guess:")))

    if guess==secret_number:
        print("congratulations!,you guessed correctly")
        break
    elif guess>secret_number:
        print("sorry,you guessed too high")
    elif guess<secret_number:
        print("sorry,you guessed too low")

attempts-=1
print("remaining attempts=",attempts)

if attempts==0:
    print("game over")
    print("the correct number was", secret_number)
