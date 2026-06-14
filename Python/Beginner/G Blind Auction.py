# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids={}
name1=input("Enter your name: ")
bid1=int(input("How much would you like to bid?\n    "))
bids[name1]=bid1
loop_gate='YES'
while loop_gate=='YES':
    print("\n"*100)
    name = input("Enter your name: ")
    bid = int(input("How much would you like to bid?\n    "))
    bids[name] = bid
    loop_gate=input("Are there any other bidders?\n'Yes' or 'No'\n    ").upper()
highest_bidder=name1
highest_bid=bid1
for i in bids:
    if bids[i]>bids[highest_bidder]:
        highest_bidder=i
        highest_bid=bids[i]
print(f"Highest bid by {highest_bidder} for {highest_bid}")
