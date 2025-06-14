import random

def welcome():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    print("Try to guess it in as few attempts as possible!")

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("❗ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("🔻 Too low. Try again.")
        elif guess > number:
            print("🔺 Too high. Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            return attempts

def main():
    best_score = None
    welcome()

    while True:
        attempts = play_game()
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🏆 New best score!")

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print(f"👋 Thanks for playing! Your best score was {best_score} attempt(s).")
            break

if __name__ == "__main__":
    main()
