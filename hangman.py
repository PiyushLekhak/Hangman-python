import random


def read_file():
    with open("words.txt", "r") as file:
        content = file.read()
    return content


def pick_random_word():
    content = read_file()
    word_list = content.split()
    return random.choice(word_list)


def is_word_guessed(chosen_word, guessed_letters):
    for letter in chosen_word:
        if letter not in guessed_letters:
            return False
    return True


def get_guessed_word(chosen_word, guessed_letters):
    word_length = len(chosen_word)
    output = ["_ "] * word_length
    for index in range(word_length):
        if chosen_word[index] in guessed_letters:
            output[index] = chosen_word[index] + " "
    return "".join(output)


def get_remaining_letters(guessed_letters):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining_letters = ""
    for letter in alphabet:
        if letter not in guessed_letters:
            remaining_letters += letter
    return remaining_letters


def play_hangman(chosen_word):
    guesses_left = 8
    guessed_letters = []
    print("\nWelcome to the game hangman")
    print(f"I am thinking of a word that is {len(chosen_word)} letters long")
    print("------------------------")

    while True:
        print("You have", guesses_left, "guesses left")
        print("Available Letters:", get_remaining_letters(guessed_letters))
        guess = input("Please guess a letter: ")

        if len(guess) != 1:
            print("Please enter only one letter")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please Enter only lowercase alphabets")
        else:
            guess = guess.lower()
            if guess in chosen_word and guess not in guessed_letters:
                guessed_letters.append(guess)
                print("Good Guess:", get_guessed_word(chosen_word, guessed_letters))
            elif guess in guessed_letters:
                print(
                    f"Oops!! {guess} has been guessed before",
                    get_guessed_word(chosen_word, guessed_letters),
                )
            else:
                print(
                    f"Oops {guess} is not in my word",
                    get_guessed_word(chosen_word, guessed_letters),
                )
                guessed_letters.append(guess)
                guesses_left -= 1
                print("_______________")

            if is_word_guessed(chosen_word, guessed_letters):
                print("Congratulations! You have won!!")
                break

            if guesses_left == 0:
                print(f"Sorry, you ran out of guesses. The word was {chosen_word}")
                break


chosen_word = pick_random_word()
play_hangman(chosen_word)
