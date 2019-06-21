import time

word_input = input("Choose a word to guess so that we can play.")

time.sleep(1)

name = input("What is your name? ")

print("Hello, " + name, "," "Time to play hangman!")

print("")

time.sleep(1)

list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]


def lister(word_input):
    return list(word_input)


dashes = "_ "
         #* len(word_input)
#print(dashes)


print("")

print("Start guessing...")
time.sleep(0.5)

print("You have six attempts!")

guess = input("guess a character:")

correct_guesses = []
wrong_list_of_guesses = []

#lowercase
chosen_word = word_input.lower()


dashes1 = []

dashes2 = lister(chosen_word)





for i in range(len(dashes2)):
    dashes1.append(dashes)


player_guess = None
turns = 6


while turns >= 1:
    if guess in list_of_letters:
        #if guess is a letter
        print("Checking...")
        time.sleep(0.1)

        if guess in dashes2:
            print("Nice. This letter is in the word.")
            position = dashes2.index(guess)
            dashes1[position] = guess
            print(dashes1)
            correct_guesses.append(guess)
            print("Right letters guessed so far: ", correct_guesses)
            print(" ")
            print("Wrong letters guessed so far: ", wrong_list_of_guesses)
            print(" ")

        elif guess not in dashes2:
            print("Sorry, this letter is not in the word.")
            print(dashes1)
            print("Right letters guessed so far: ", correct_guesses)
            wrong_list_of_guesses.append(guess)
            print(" ")
            print("Wrong letters guessed so far: ", wrong_list_of_guesses)
            print(" ")
            turns -= 1
            print("You have "+str(turns)+" more guesses.")

        elif len(dashes2) == len(correct_guesses):
            print("You win!")
            break
        else:
            print("Error")
        guess = input("guess another character:")
    else:
        print("Try entering a letter.")


print("You Lose")

