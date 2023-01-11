# importing my required modules
import random
import hangman_art
import hangman_words
import os

# beginning program
selected_word = random.choice(hangman_words.word_list)
word_length = len(selected_word)
end_of_game = False
total_lives = 6

print(f"The chosen word is :{selected_word}")
# printing my ascii logo for good aesthetics
print(hangman_art.cover_logo)

# creating our blanks
display = []
for _ in range(0, word_length):
    display += "_"

# beginning  our program flow
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if user has entered a letter they have already guessed , print the letter and let them know
    if guess in display:
        print(f"you have already guessed the letter {guess}")

    # check guessed letter
    for letter_position in range(0, word_length):
        letter = selected_word[letter_position]
        if letter == guess:
            display[letter_position] = letter

    # clear the terminal to make our screen look neater during program
    os.system("clear")
    # checking if user is wrong
    if guess not in selected_word:
        print(f"You guessed {guess}, thats not in the word .You lose a life.")
        total_lives -= 1
        if total_lives == 0:
            end_of_game = True
            print("you lose")

    # join all elements in the list and turn it into a string
    print(f"{''.join(display)}")

    # check if user has got all the letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    # used the stages from hangman_art.py
    print(hangman_art.stages[total_lives])
