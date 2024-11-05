from random import randint

def guess_number_game():

    while True:
        # CPU Chooses a Number Between 1 and 100
        target_number = randint(1, 100)
        # User Input Initially None for Checking in Loop
        user_guess = None
        # User Attempts First Is 0
        attempts = 0

        while user_guess != target_number:
            # This Loop Check User Guess And CPU Guess
            try:
                user_guess = int(input("Guess a number between 1 and 100(You Have 10 Chance For Guess): "))
                if user_guess < 1 or user_guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue
                # If User Guess Doesn't Match CPU Guess, Increment Attempts
                attempts += 1
                if user_guess < target_number:
                    print("Your guess is too low!")
                elif user_guess > target_number:
                    print("Your guess is too high!")
                if attempts >= 10:
                    print(f"Too many guesses! The correct number was {target_number}.")
                    break

            except ValueError:
                print("Please enter a valid number.")


        if user_guess == target_number:
            # If CPU + User Print(Correct)

            print(f"Congrats! You guessed the correct number in {attempts} attempts!")
        else:
            # If User Can't Guess Correctly After 10 Attempts, They Lose!
            print(f"Sorry You Lose, you guessed the wrong number in {attempts} attempts!")


            while True:
                # After Play (Win Or Lose) Ask Of User Need continue?
                play_again = input("Do you want to play again? (yes/no): ").lower()
                # If User Type yes continue Or Type no Exit The Game!!!
                if play_again == "yes":
                    break

                elif play_again == "no":
                    print("Thank you for playing!")
                    return
                # If User Type Wrong Give Message For Try Again
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")


# For Call Function
guess_number_game()
