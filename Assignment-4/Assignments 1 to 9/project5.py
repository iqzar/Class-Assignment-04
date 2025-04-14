import random
import string
from words import words  # your list of words from words.py

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    print("🎮 Welcome to Hangman!")
    print(f"You have {lives} lives. Let's begin!")

    # game loop
    while len(word_letters) > 0 and lives > 0:
        # show used letters
        print("\nUsed letters:", " ".join(sorted(used_letters)))

        # show current word progress
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_display))

        # get user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Good guess!")
            else:
                lives -= 1
                print(f"❌ Wrong guess. You lost a life. Lives left: {lives}")
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try again.")
        else:
            print("🚫 Invalid character. Please try a valid letter.")

    # game end
    if lives == 0:
        print(f"\n💀 You died! The word was: {word}")
    else:
        print(f"\n🎉 You guessed the word: {word}!")


# Run the game
if __name__ == '__main__':
    hangman()
