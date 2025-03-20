import numpy as np
from utils import player_actions

players = [
    [62, 56, 57, 58, 48, 61, 59, 63, 60, 54, 51],
    [125, 121, 112, 120, 127, 122, 124, 107, 111, 113, 115, 123, 116, 118, 119, 126]
]

level_7 = []
for player in players[0]:  
    actions = player_actions(player)[1:7]
    level_7.append(actions)

level_7_np = np.array(level_7)
level_7_dist = np.mean(level_7_np, axis=0)
print("Target 7 Best Actions")
for i in range(len(level_7_dist)):
    print(f"- Level {i+1}: {level_7_dist[i]}")

print("")

level_8 = []
for player in players[1]:  
    actions = player_actions(player)[1:8]
    level_8.append(actions)

level_8_np = np.array(level_8)
level_8_dist = np.mean(level_8_np, axis=0)
print("Target 8 Best Actions")
for i in range(len(level_8_dist)):
    print(f"- Level {i+1}: {level_8_dist[i]}")