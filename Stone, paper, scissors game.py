import random

options=("stone","paper","scissors")
is_running=True

while is_running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice (stone, paper, scissors): ")
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player==computer:
        print("It's a tie!")
    elif player=="paper" and computer=="stone":
        print("You Win!")
    elif player=="stone" and computer=="scissors":
        print("You Win!")
    elif player=="scissors" and computer=="paper":
        print("You Win!")
    else:
        print("You lose.")

    if not input("Play again? (y/n): ").lower()=="y":
        is_running=False
        
print("Thanks for playing!")