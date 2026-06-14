import random
player_move=input("Rock(R), Paper(P), Scisscors(S). Which do you choose?\n").upper()
moves=["R","P","S"]
computer_move=(random.choice(moves)).upper()
if player_move==computer_move:
    print(f"You chose {player_move}\nComputer  {computer_move}\nIt's a draw.")
else:
    if player_move=="R" and computer_move=="S":
        print(f"You chose {player_move}\nComputer chose {computer_move}\nYou Win!")
    elif player_move=="R" and computer_move=="P":
        print(f"You loose.\nYou chose {player_move}\nComputer chose {computer_move}")
    elif player_move=="S" and computer_move=="P":
        print(f"You chose {player_move}\nComputer chose {computer_move}\nYou Win!")
    elif player_move=="S" and computer_move=="R":
        print(f"You loose.\nYou chose {player_move}\nComputer chose {computer_move}")
    elif player_move=="P" and computer_move=="R":
        print(f"You chose {player_move}\nComputer chose {computer_move}\nYou Win!")
    elif player_move=="P" and computer_move=="S":
        print(f"You loose.\nYou chose {player_move}\nComputer chose {computer_move}")
    else:
        print("Choose either R, P, or S only.")
