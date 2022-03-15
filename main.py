import random, os
from termcolor import colored

os.system("color")
clear = lambda: os.system("cls")

def word():
    with open("words.txt") as r:
        lst = [word.replace("\n", "") for word in r.readlines()]
    return random.choice(lst)

def main(w):
    attempts = 0
    letters = []
    while attempts < 6:
        guess = input(f"\nAttempt: {attempts + 1}\nGuess: ")
        if len(guess) != 5:
            print(colored("\nGuess must be a five letter word!", "red"))
            continue
        if guess == w:
            print(colored(w, "green"))
            break
        else:
            for x in range(5):
                letters.append(guess[x])
                if guess[x] == w[x]:
                    print(end=colored(guess[x], "green"))
                elif guess[x] in w:
                    print(end=colored(guess[x], "yellow"))
                else:
                    print(end="_")
        print("\nGuessed letters: ", end="")
        [print(end=colored(f"{l}", "green")) if l in w else print(end=colored(f"{l}", "red")) for l in set(letters)]
        attempts += 1
    print(colored(f"\nThe word was: {w}\n\n", "green"))
    
if __name__ == "__main__":
    while True:
        choice = input("[1] Play\n[2] Quit\nChoice: ")
        if choice == "1":
            clear()
            main(word())
        elif choice == "2":
            quit()
        else:
            clear()