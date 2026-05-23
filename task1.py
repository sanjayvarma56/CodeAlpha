import random
def play_hangman():
    words = ["apple","banana","grape","orange","mango","kiwi"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    incorrect_attempts = 8
    while incorrect_attempts > 0 and "_" in guessed_word:
        print("Current word: " + " ".join(guessed_word))
        print("Guessed letters: " + ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess not in guessed_letters:
            guessed_letters.append(guess)
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Correct!")
        else:
            incorrect_attempts -= 1
            print("Wrong! Incorrect attempts left: " + str(incorrect_attempts))
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word: " + word)
            print("Game Over!\nThe word was also : " + word)
            break
    if incorrect_attempts == 0:
        print("Game over! The word was: " + word)
play_hangman()
