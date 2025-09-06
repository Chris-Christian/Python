import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art=  {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│ ●       │",
                "│         │",
                "│       ● │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│ ●       │",
                "│    ●    │",
                "│       ● │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘")}

total=0
num_of_dice=input("Enter number of dice: ")

while not num_of_dice.isdigit() or int(num_of_dice)<1:
    num_of_dice=(input("Please enter a valid number of dice: "))

num_of_dice=int(num_of_dice)

for die in range(num_of_dice):
    roll=random.randint(1,6)
    for line in dice_art[roll]:
        print(line)
    total+=roll

print(f"Total: {total}")