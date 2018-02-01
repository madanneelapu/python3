import random

guess = random.randint(0,100)
print("My Guess is :",guess)

attempt = 0
while attempt < 3:
    ans = input("Enter your guess :")
    ans = int(ans)
    attempt += 1
    if ans == guess:
        print("Voila, Your guess is right!!")
        break

else:
    print("Mission Failed")