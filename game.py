import sys
import numpy as np

# Problem Setup
num_doors = int(sys.argv[1]) if len(sys.argv) > 1 else 3
prize_door = np.random.choice(num_doors)

# Choice
choice = input(f"Choose a door number between 0 and {num_doors - 1}: ")
while not choice.isdigit() or int(choice) < 0 or int(choice) >= num_doors:
    choice = input(f"Choose a door number between 0 and {num_doors - 1}:")
choice = int(choice)

# More Information
if prize_door == choice:
    sudo_prize_door = np.random.choice(num_doors - 1)
    if sudo_prize_door >= choice:
        sudo_prize_door += 1
else:
    sudo_prize_door = prize_door

for i in range(num_doors):
    if i != choice and i != sudo_prize_door:
        print(f"Door {i} is empty")

# Switch?
flip = input(f"Do you want to switch to door {sudo_prize_door}? (Y/n) ").lower() == "y"

if flip:
    choice = sudo_prize_door

# Results
if choice == prize_door:
    print(f"Congrats! You won a million dollars! The prize was in door {choice}")
else:
    print(f"Sorry door {choice} was empty. The prize was in door {prize_door}")