import random


def generateNumber(start, end):
    return random.randint(start, end)

def guessNumber():
    play_again = True

    while play_again:
        attempts = 5
        counter = 0
        sn = generateNumber(1,100)
        while counter < attempts:
            try:
                guess = int(input(f"Guess a number between 1 and 100: {attempts-counter} remaining attempt(s).\n"))
                if guess < 1 or guess > 100:
                    print("Invalid number, the number should be between 1 and 100.\n")
                    continue
                if guess > sn:
                    print("The number is lower.")
                elif guess < sn:
                    print("The number is greater.")
                else:
                    print("Congratulations, you got it! The number was:", sn)
                    break
                counter += 1
            except ValueError:
                print("The value inputted isn't an integer.\n")
        else:
            print("You lose! The secret number was:", sn)
        again = input("Do you wanna play again? (y/n)\n")
        if again.lower() != 'y':
            play_again = False

# Initialization      
guessNumber()