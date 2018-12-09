from itertools import cycle
from collections import deque

num_players = 465
num_marbles = (71498)*100

available_marbles = [i for i in range(num_marbles, 0, -1)]
# print("available_marbles :{}".format(available_marbles))

players = cycle([i for i in range(1, num_players + 1)])

players_scores = [0 for i in range(num_players)]
print('players_scores: {}'.format(players_scores))

# create the deque object and add the first marble ...
marbles_placed = deque([0])

for i in range(1, num_marbles + 1):
    player = next(players)
    # print('player: {}'.format(player))
    if i % 23 == 0:
        marbles_placed.rotate(7)
        # remove the marble, but don't add it to the marbles_placed
        score = available_marbles.pop() + marbles_placed.pop()
        players_scores[player - 1] += score
        # print("playter: {}  score!: {}  total: {}".format(player, score, players_scores[player - 1]))
        # rotate the list one to the left still
        marbles_placed.rotate(-1)
    else:
        # rotate the list one to the left, and place the next marble on the end of the list
        marbles_placed.rotate(-1)
        marbles_placed.append(available_marbles.pop())
        
    # print('marbles_placed: {}'.format(marbles_placed))
    # print('---\n')

print('players_scores: {}'.format(players_scores))
print("max score: {}".format(max(players_scores)))
