import random

def guessANumber():
    computer = random.randint(1, 10)
    playerAttempts = 0  # Initialize attempts in this function
    while True:
        player = int(input("Choose a number between 1 and 10: "))

        if player == computer:
            print("You win!")
            return playerAttempts + 1  # Return the number of attempts + 1 for the winning guess
        elif player < computer:
            print ("Try a higher number")
        else:
            print("Try a lower number")
            
        playerAttempts += 1  # Increment attempts in this function



def attemptsMade():
    totalAttempts = 0  # Initialize total attempts

    while True:
        attempts = guessANumber()
        totalAttempts += attempts
        print(f"Thanks for playing! You made {attempts} attempts this game.")

        question = input("Would you like to play again? (yes/no): ")
        if question.lower() == "yes":
            print("Ok, Have Fun!")
        else:
            print(f"Thanks for playing in total! You made {totalAttempts} attempts.")
            break

# Main Code 
attemptsMade()



















