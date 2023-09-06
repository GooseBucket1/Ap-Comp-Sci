import random 

def letsPlay(): # the function letsPlay givess you the prompt: Choose Rock paper or scissors then the computer chooses  
    player = input("Choose rock (r), paper (p), or scissors(s): ")
    computer = random.choice(['r', 'p', 's'])

    if player == computer: # if you and the computer got the same answers then it will tell you that you tied
        return "That's rare... you tied"

    if isWin(player, computer): # if you choose a one that beats the computer it will tell you that you won 
        return "Wow You Won"

    if isWin(computer, player): # if the computer chooses one that beats you it will tell you that you lost
        return "Sadly you lost... too bad"

    return "Invalid choice. Please choose 'r', 'p', or 's'."

def isWin(player, opponent): # this tells which beats which like rock beats scissors 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

# playAgain will pop up after your first round and will ask you if you would like to play again if yes it will ask you  rock, paper,
# or scissors  if no it will end the game and display your score
def playAgain():
    playerScore = 0
    computerScore = 0

    while True:
        response = input("Would you like to play again? (yes/no): ")
        if response.lower() == "yes":
            result = letsPlay()
            print(result)  # Print the result here

            if "Wow You Won" in result:
                playerScore += 1
            elif "Sadly you lost... too bad" in result:
                computerScore += 1

            print(f"Player: {playerScore}, Computer: {computerScore}")
        elif response.lower() == "no":
            break



# main code
playAgain()


