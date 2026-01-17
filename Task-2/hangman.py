word = "python"
guessed = ""
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    missing = 0

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            missing += 1

    print()

    if missing == 0:
        print("You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed += guess

    if guess not in word:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)
