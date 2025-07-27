import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0 - 9, adn you have to guess which number I am going to say one digit at a time")
print("The game ends when you get one correct!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game!")
        print("And the number was...")
        print(number)
        break
    else:
        print("Your guess isn't right")
        print("Try again!")