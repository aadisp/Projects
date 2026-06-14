print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

if input("Which way do you choose, left or right?").lower()=="right":
   if input('You\'re at the bank of a river. Would you like to wait for a boat(w) or would you rather to swim(s)?').lower()=="w":
       last=input("You have crossed the river, and now standing in front of three doors- Red(r), Blue(b), and Yellow(y). Which door will you enter?").lower()
       if last=="y":
           print("You found the treasure! You win!!")
       elif last=="r":
           print("You were engulfed by fire.\nGame Over")
       elif last=="b":
           print("You were devoured by beasts.\nGame Over")
       else:
           print("Game Over")
   else:
       print("You were attacked by a trout.\nGame Over")
else:
    print("You fell into a hole.\nGame Over")
