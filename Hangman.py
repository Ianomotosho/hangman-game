import random

# my word list of secret words
word_list = ["my","head","hurts","badly","python","hangman"]

# this is to select a word to my word list
secret_word  = random.choice(word_list)

#making variables to build the hangman if someone gets it wrong
correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

# this is to show  the current game status
def display_game_state():
    # display the secret word with guessed letters revealed
    displayed_word = "". join([letter if letter in correct_guesses else "_" for letter in secret_word])
    print(f"word: {displayed_word}")
    print(f"Incorrect guesses: {''.join(incorrect_guesses)}")
    print(f"attempts left: {attempts_left}")

# main game loop
while True:
    display_game_state()
    guess = input("Enter your guess: ").lower()
    #to check if the guess is right
    if guess in secret_word:
        correct_guesses.add(guess)
        #check for win condition 
        if set(secret_word).issubset(correct_guesses):
            print("Congratulations you guessed the word")
            break
    else:
        incorrect_guesses.add(guess)
        attempts_left -= 1
        #check for lose condition
        if attempts_left == 0:
            print("game over! you've ran out of attemps.")
            print(f"The secret word was: {secret_word}")
            break