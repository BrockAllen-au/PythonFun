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
                print("Too low! Try a bigger number\n")
                guesses += 1
            elif guess > number:
                print("Too big! Try a lower number\n")
                guesses += 1
        except:
            print("Please enter a valid whole number only.\n")

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
        if accuracy == 100:
            print(f"Holy shit! How lucky are you?! Guessing accuracy of {round(accuracy,2)}%!")
        elif accuracy < 100 and accuracy > 80:
            print(f"Wowee! You're pretty good at this whole guessing thing ha!?\nGuess Accuracy: {round(accuracy,2)}%!")
        elif accuracy < 80 and accuracy > 50:
            print(f"Eh you're an alright guesser I suppose. Guess accuracy: {round(accuracy,2)}%")
        elif accuracy < 50 and accuracy > 20:
            print(f"What grade did you drop out of school?! My 3 year old niece can guess better than you!"
                  f"\nGuess accuracy: {round(accuracy,2)}%")
        elif accuracy < 20:
            print(f"You're about as useful as a cock flavoured lollipop!"
                  f"\nA measly guess accuracy of {round(accuracy,2)}%!")
        time.sleep(5)
        game_active = False
    else:
        continue
