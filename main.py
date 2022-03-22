import random, os
from termcolor import colored
from dictionary import definition

os.system("color")
clear = lambda: os.system("cls")

def word():
    with open("words.txt") as r:
        lst = [word.strip("\n") for word in r.readlines()]
    return random.choice(lst).lower()

def main(wrd):
    attempts = 0
    letters = []
    guesses = []
    while attempts < 6:
        w = list(wrd)
        guess = input(f"\n\nAttempt: {attempts + 1}\nGuess: ").lower()
        clear()
        out = ["", "", "", "", "",]
        if len(guess) != 5:
            print(colored("\nGuess must be a five letter word!", "red"))
            for item in guesses:
                print(item)
            print("Guessed letters: ", end="")
            [print(end=colored(f"{l}", "green")) if l in wrd else print(end=colored(f"{l}", "red")) for l in sorted(set(letters))]
            continue
        if guess == wrd:
            for item in guesses:
                print(item)
            print(colored(wrd, "green"))
            print("Guessed letters: ", end="")
            [print(end=colored(f"{l}", "green")) if l in wrd else print(end=colored(f"{l}", "red")) for l in sorted(set(letters))]
            break
        else:
            with open("words.txt") as read:
                if not guess in read.read():
                    print(colored("Not a valid word!", "red"))
                    for item in guesses:
                        print(item)
                    print("Guessed letters: ", end="")
                    [print(end=colored(f"{l}", "green")) if l in wrd else print(end=colored(f"{l}", "red")) for l in sorted(set(letters))]
                    continue
            for x in range(5):
                letters.append(guess[x])
                if guess[x] == w[x]:
                    out[x] = (colored(guess[x], "green"))
                    w[w.index(guess[x])] = ""
                elif guess[x] in w:
                    out[x] = (colored(guess[x], "yellow"))
                else:
                    out[x] = (colored(guess[x], "red"))
            guesses.append("".join(out))
            for item in guesses:
                print(item)
        print("Guessed letters: ", end="")
        [print(end=colored(f"{l}", "green")) if l in wrd else print(end=colored(f"{l}", "red")) for l in sorted(set(letters))]
        attempts += 1
    print(colored(f"\nThe word was: {wrd}", "green"))
    try:
        defi = definition(wrd)
        print(colored(f"{defi['type']}\n{defi['def']}", "yellow"))
    except:
        print(colored("Unable to find definition of word!", "red"))
    remove = input(f"Do you want to remove {wrd} from the list of valid words? (y/N): ")
    if remove.lower() == "y":
        with open("words.txt", "r") as read:
            lines = read.readlines()
        with open("words.txt", "w") as write:
            for line in lines:
                if line.strip("\n") != wrd:
                    write.write(line)
    
if __name__ == "__main__":
    while True:
        choice = input("\n[1] Play\n[2] Custom word\n[3] Quit\nChoice: ")
        if choice == "1":
            clear()
            main(word())
        elif choice == "2":
            clear()
            while True:
                custom = input("Custom five letter word: ")
                if len(custom) == 5:
                    with open("words.txt", "r+") as read:
                        if not custom in read.read():
                            wrdAdd = input(colored("Word not found in list, would you like to add it? (y/N): ", "green"))
                            if wrdAdd.lower() == "y":
                                read.write(f"\n{custom}")
                    main(custom)
                    break
                else:
                    print(colored("Must be five letters!", "red"))
        elif choice == "3":
            quit()
        else:
            clear()
