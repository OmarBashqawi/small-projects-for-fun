import random as rand

# Instance Variales better if you wanted to change the values
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# We did this so we don't have ths value written twice one in dict andone in tuple
emojis = {ROCK : "🪨", PAPER : "📄", SCISSORS : "✂️"}
list = tuple(emojis.keys())

#display the user choice rock,paper or scissors
def display_choices(choice, computer_choice):
    print(f"You Chose {emojis[choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    
#display if the user won or lost
def rock_paper_scissors_game(choice, computer_choice):
    if choice == computer_choice:
        return "Draw!"
    elif (
        (choice == ROCK and computer_choice == SCISSORS) or
        (choice == SCISSORS and computer_choice == PAPER) or
        (choice == PAPER and computer_choice == ROCK)):
        return "You Won!"
    else:
        return "You lose!"
        
def main():

        while True:
            user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
            computer_choice = rand.choice(list)
            if user_choice in list:
                display_choices(user_choice, computer_choice)
                print(rock_paper_scissors_game(user_choice, computer_choice))
                ask = input("Continue? (y/n)").lower()
                if ask == "n":
                    break
            else:
                print("Invalied Value!, Please Try again")

        
main()