import random
import time

# A quick game that will get a user to guess a number between 1 and 1,000.

number_range = range(1, 1000)

guesses = 0
total_guesses = 0
games_played = 0

game_active = True

while game_active:
    number = random.choice(number_range)
    print("I'm thinking of a number from 1 to 1,000. Can you guess it?")
    guess = 0
    while guess != number:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
            if guess <= 0 or guess > 1000:
                print("Please enter a number from 1 to 1,000")
            elif guess < number:
                print("Too low! Try a bigger number")
                guesses += 1
            elif guess > number:
                print("Too big! Try a lower number")
                guesses += 1
        except:
            print("Please enter a valid whole number only.")

    guesses += 1
    print(f"Well done! You guessed it! The number I was thinking of was {number}!")
    print(f"It took you {guesses} guesses to find my number.")

    total_guesses = total_guesses + guesses
    guesses = 0
    games_played += 1
    print(f"Games played: {games_played}")
    print(f"Total guesses: {total_guesses}")

    play_again = input(str("Press Enter to play again, or type 'quit' to exit. ")).lower()
    if play_again == 'quit':
        print("Thanks for playing!")
        print(f"You played a total of {games_played} games and made {total_guesses} total guesses!")
        accuracy = games_played / total_guesses * 100
        print(f"That's a guessing accuracy of: {round(accuracy,2)}% !")
        time.sleep(5)
        game_active = False
    else:
        continue
