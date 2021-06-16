import sys
import numpy as np

num_doors = int(sys.argv[1]) if len(sys.argv) > 1 else 3
num_runs = int(sys.argv[2]) if len(sys.argv) > 2 else 100
flip_policy = sys.argv[3].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'] if len(sys.argv) > 3 else True

def simulate(flip=True):
    # Problem Setup
    prize_door = np.random.choice(num_doors)

    # Choice
    choice = np.random.choice(num_doors)

    # More Information
    if prize_door == choice:
        sudo_prize_door = np.random.choice(num_doors - 1)
        if sudo_prize_door >= choice:
            sudo_prize_door += 1
    else:
        sudo_prize_door = prize_door

    # Switch?
    if flip:
        choice = sudo_prize_door

    # Results
    return choice == prize_door

win_count = 0
for _ in range(num_runs):
    if simulate(flip=flip_policy):
        win_count += 1

print(f"Won {win_count} of {num_runs} games, which is about {100 * win_count / num_runs}% of the games.")