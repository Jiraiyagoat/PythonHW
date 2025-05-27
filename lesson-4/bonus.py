import random
options = ['rock', 'paper', 'scissors']
win_rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
me, comp = 0, 0
while True:
    c_choice = random.choice(options)
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    print(f"Computer chose: {c_choice}")
    if choice == c_choice:
        print("It's a draw.")
    elif win_rules[choice] == c_choice:
        me += 1
        print("You won this round.")
    else:
        comp += 1
        print("I won this round.")
    print(f"Score -> You: {me} | Me: {comp}\n")
    if me == 5:
        print("🎉 You won the match!")
        break
    elif comp == 5:
        print("😢 You lost the match!")
        break
