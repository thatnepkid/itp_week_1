# Rock, Paper, Scissors

import random

while True:
    user_hand = input("Enter your move (Rock, Paper, Scissors): ")
    cap_user_hand = user_hand.capitalize()

    moves = ["Rock","Paper","Scissors"]
    comp_move = random.choice(moves)

    print("You chose " + cap_user_hand + ", the computer chose " + comp_move + ".")

    if cap_user_hand == comp_move:
        print("It is a tie.")
    elif cap_user_hand == "Rock":
        if comp_move == "Scissors":
            print("Rock smashes scissors! You win.")
        else:
            print("Paper covers rock! You lose.")
    elif cap_user_hand == "Paper":
        if comp_move == "Rock":
            print("Paper covers rock! You win.")  
        else:
            print("Scissors cuts paper! You lose.")      
    elif cap_user_hand == "Scissors":
        if comp_move == "Paper":
            print("Scissors cuts paper! You win.") 
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (Y/N): ")
    cap_play_again = play_again.capitalize()
    if cap_play_again != "Y":
        break