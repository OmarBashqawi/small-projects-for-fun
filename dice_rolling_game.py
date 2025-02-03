import random as rand

def start_game(answer):
    dice_1 = [1,2,3,4,5,6]
    dice_2 = [1,2,3,4,5,6]

    if answer == "y":
        return rand.choice(dice_1), rand.choice(dice_2)
    elif answer == "n":
        return "Thanks for playing!"
    else:
        return "Invalid Answer!"


def main():

    while True:
        start = input("Role the dice? (y/n)").lower()
        print(start_game(start))
        if start == "n":
            break

main()