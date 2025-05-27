import random
while True:
    num = random.randint(1, 100)
    for i in range(10):
        guess = int(input("Guess the number (1-100): "))
        if guess == num:
            print("You guessed it right!")
            break
        elif guess > num:
            print("Too high!")
        else:
            print("Too low!")
    else:
        print("You lost. Want to play again?")

    again = input("Play again? (Y/YES/y/yes/ok): ")
    if again not in ['Y', 'YES', 'y', 'yes', 'ok']:
        print("Goodbye!")
        break
