import random
import game_data

data=game_data.data
def play():
    print("\n" * 200)
    score=0
    print("Score: 0\n")

    A=random.choice(data)

    def game(A,score):
        B=random.choice(data)

        while A==B:
            B=random.choice(data)

        print(f"A: {A['name']}, {A['description']}, {A['country']}.")
        print(f"B: {B['name']}, {B['description']}, {B['country']}.\n")

        if A['follower_count']>B['follower_count']:
            ans="A"
        else:
            ans="B"

        choice=input("Who has more number of followers: A or B?\n   ").upper()
        A = B
        if choice==ans:
            print("\nYou are right.")
            score+=1
            print(f"Current score: {score}.")
            game(A,score)
        else:
            print(f"You lose.\n\nFinal Score: {score}")
            if input("Press Enter to play again: ")=='':
                print("\nYour score has been reset.")
                play()

    game(A,score)

play()
