import random as rand

random_number = rand.randint(1, 100)
def guessing_game(num):
    if num > random_number:
        return "Two High!"
    elif num < random_number:
        return "Two Low!"
    else:
        return "Congratulations! You guessed the number."

def main():

    while True:
        try:
            ask = int(input("Guess the number between 1 and 100: "))
            print(guessing_game(ask))
            if ask == random_number:
                break
        except ValueError:
            print("Invalied Number!")
        
main()
