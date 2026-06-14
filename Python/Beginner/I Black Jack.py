import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10]

will="Yes"

def hit(playerHand,playerTotal,dealerHand,dealerTotal):
    card=random.choice(cards)
    if card==11 and playerTotal+card>21:
        card=1
    playerHand+=[card]
    playerTotal=sum(playerHand)
    print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand[0]}] ---> ({dealerTotal})\n------------")
    if playerTotal>21:
        dealerTotal = sum(dealerHand)
        print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand}] ---> ({dealerTotal})\n------------")
        print("Bust")
    elif playerTotal==21:
        dealerTotal = sum(dealerHand)
        print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand}] ---> ({dealerTotal})\n------------")
        if dealerTotal==21:
            print("Push")
        elif dealerTotal<21:
            print("Player Wins")
    return playerHand, playerTotal, dealerHand, dealerTotal

def stand(playerHand,playerTotal,dealerHand,dealerTotal):
    dealerTotal=sum(dealerHand)
    print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand}] ---> ({dealerTotal})\n------------")
    while dealerTotal<17:
        card = random.choice(cards)
        if card == 11 and dealerTotal + card > 21:
            card = 1
        dealerHand+=[card]
        dealerTotal=sum(dealerHand)
        print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand}] ---> ({dealerTotal})\n------------")
    if dealerTotal>21:
        print("Dealer Bust. Player Wins")
    else:
        if playerTotal>dealerTotal:
            print("Player wins.")
        elif playerTotal<dealerTotal:
            print("Dealer Wins.")
        else:
            print("Push")
    playerTotal=21
    return playerHand, playerTotal, dealerHand, dealerTotal

while will=="Yes":
    print("\n"*200)
    pcard = random.choice(cards)
    if pcard == 11 and dealerTotal + pcard > 21:
        pcard = 1
    dcard = random.choice(cards)
    if dcard == 11 and dealerTotal + dcard > 21:
        dcard = 1
    playerHand=[random.choice(cards),pcard]
    dealerHand=[random.choice(cards),dcard]
    playerTotal=sum(playerHand)
    dealerTotal=dealerHand[0]
    print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand[0]}] ---> ({dealerTotal})\n------------")
    if playerTotal==21:
        dealerTotal = sum(dealerHand)
        print(f"Player Hand: {playerHand} ---> ({playerTotal})\nDealer Hand: [{dealerHand}] ---> ({dealerTotal})\n------------")
        if dealerTotal==21:
            print("Push")
        elif dealerTotal<21:
            print("Player Wins")
    while playerTotal<21:
        move=input("Hit-[H] or Stand-[S]:\n   ").upper()
        if move=="H":
            playerHand,playerTotal,dealerHand,dealerTotal=hit(playerHand,playerTotal,dealerHand,dealerTotal)
        elif move=="S":
            playerHand,playerTotal,dealerHand,dealerTotal=stand(playerHand,playerTotal,dealerHand,dealerTotal)

    will=(input("Wish to play another game?\n 'Yes' to play\n 'No' to stop\n")).title()

print("Thankyou")
