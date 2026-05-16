import random

best_score = None

def choose_difficulty():
    print("\nSelect Difficulty Level")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("Invalid choice. Please try again.")

def play_game():
    global best_score

    max_range = choose_difficulty()

    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🎉 New Best Score!")

                print(f"Best Score: {best_score} attempts")
                break

        except ValueError:
            print("Please enter a valid number.")

while True:
    play_game()

    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("\nThank you for playing!")
        break