import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = "python"

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
wrong_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_attempts - wrong_guesses)

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)