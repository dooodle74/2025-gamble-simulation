import sys
from utils import player_actions

if len(sys.argv) < 2:
    print("Usage: python script.py <player> [target]")
    sys.exit(1)

player = int(sys.argv[1])
target = int(sys.argv[2]) if len(sys.argv) > 2 else 8  

actions = player_actions(player)[1:target]
print(actions)