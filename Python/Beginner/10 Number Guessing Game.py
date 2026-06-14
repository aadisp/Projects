import random

def game():
    number=random.randint(1,100)
    print("A number among numbers 1 to 100 is chosen.")
    mode=input("Choose a difficulty:\n  Easy [E]\n  Hard [H]\n").lower()
    if mode=="e":
        g=10
        print("You've got 10 chances to guess the right number.")
    elif mode=="h":
        g=5
        print("You've got 5 chances to guess the right number.")
    life="alive"
    while life=="alive":
        guess=int(input("Guess the number: "))
        if guess==number:
            print("You guessed right.")
            life = "dead"
            will = input("Do you wish to play another game:\n  Yes [Y]\n  No [N]\n").lower()
            if will == "y":
                print("\n" * 200)
                game()
        else:
            if guess>number:
                print("You guessed too high.")
            else:
                print("You guessed too low.")
            g-=1
            if g==0:
                print(f"You've run out of guesses.\nThe right answer was {number}.")
                life="dead"
                will=input("Do you wish to play another game:\n  Yes [Y]\n  No [N]\n").lower()
                if will=="y":
                    print("\n"*200)
                    game()
                else:
                    life="dead"
            else:
                print(f"You're left with {g} guesses.")

game()

print("Thank you.")
