import random
def get_computer_choice(): 
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice(): 
    user_choice = input("Enter your choice ")
    return user_choice

def get_winner(computer_choice, user_choice): 
    #winner = ""
    if computer_choice == "Rock":
        if user_choice == "Rock":
            print("It is a tie!")
            #winner = "tie"
        elif user_choice == "Paper":
            print("You won!")
            #winner = "you"
        else: 
            print("You lost")
            #winner = "computer"
    elif computer_choice == "Paper": 
        if user_choice == "Rock":
            print("You lost")
            #winner = computer
        elif user_choice == "Paper":
            print("It is a tie!")
            #winner = "tie"
        else: 
            print("You won!")
            #winner = "user"
    else: 
        if user_choice == "Rock":
            print("You won!")
            #winner = "user"
        elif user_choice == "Paper":
            print("You lost")
            #winner = "computer"
        else: 
            print("It is a tie!")
            #winner = "tie"

    # return winner

def play(): 
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()

