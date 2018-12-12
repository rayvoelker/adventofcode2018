import re
import pdb
from collections import deque

initial_state = "#........#.#.#...###..###..###.#..#....###.###.#.#...####..##..##.#####..##...#.#.....#...###.#.####"
input = """
#..## => .
##..# => #
..##. => .
.##.# => #
..... => .
..### => #
###.# => #
#.... => .
#.##. => #
.#.## => #
#...# => .
...## => .
###.. => #
.#..# => .
####. => .
....# => .
##### => #
.###. => .
#..#. => .
##... => #
.#... => #
#.#.# => .
..#.. => #
...#. => #
##.#. => .
.##.. => #
.#.#. => .
#.#.. => .
..#.# => #
#.### => .
##.## => .
.#### => #
"""

# example ...
# initial_state = "#..#.#..##......###...###"
# input = """
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #
# """

# turn the initial_state string into a list of characters
pots = deque(initial_state)
print(pots)

rule = dict({
    'test': '',
    'result': ''
})

rules = list()

# count removed from front list
c = list()

# create the rules list...
input = input.strip().split('\n')
for item in input:
    # print(item)
    temp = re.split(r"^(.{5}).{4}(.{1})", item)
    rules.append(rule.copy())
    rules[-1]['test'] = temp[1]
    rules[-1]['result'] = temp[2]
print(rules)

# grow the array so that we have 4 empty pots on each end ...
def grow_pots():
    pots.appendleft('.')
    pots.appendleft('.')
    pots.appendleft('.')
    pots.appendleft('.')
    pots.append('.')
    pots.append('.')
    pots.append('.')
    pots.append('.')


def trim_pots():
    # first trim from the left ...
    # for i in range(len(pots)):
    count_removed_left = 0
    while pots[0] == '.':
        pot = pots.popleft()
        count_removed_left +=1
        # print('removed: {}'.format(pot))

    print('count_removed_left: {}'.format(count_removed_left))

    while pots[-1] == '.':
        pot = pots.pop()
        # print('removed: {}'.format(pot))

    return count_removed_left

# pots at gen 0
print('starting length: {}'.format)
print(''.join(pots))

for gen in range(20):

    grow_pots()

    # pot to store our next gen in ...
    temp_pots = pots.copy()
    # for rule in rules:

    for i in range(2, len(pots) - 2):
        slice_start = i - 2
        slice_end = i + 2
        # print('i: {}'.format(i))
        # print('slice start: {}'.format(slice_start))
        # print('slice end: {}'.format(slice_end))

        # convert the array slice to a string, so we can compare to our rule
        sample = ''.join(list(pots)[i-2:i+3])
        # print('test:    {}'.format(rules[1]['test']))
        # print('sample:  {}'.format(sample))
        # print('---')

        rule_count = 0
        for rule in rules:
            if sample == rule['test']:
                # print('match ... {} == {}'.format(sample, rule['test']))
                temp_pots[i] = rule['result']
                rule_count += 1

        # print('matched rules: {}'.format(rule_count))
        if rule_count == 0:
            temp_pots[i] = '.'
        
    # replace the temp copy with the current version
    pots = temp_pots.copy()
    count_removed = trim_pots()
    c.append(count_removed)

    print(''.join(pots))

print("minimum removed from left: {}".format(min(c)))
# start counting at min(c) - 1
# start_count = (min(c) - 1) * -1

start_count = -1
print("start index count at: {}".format(start_count))

# 3159 at start index count = -2 .. not right ...
# 3217 at start index count = -1 .. is the correct answer

count = 0
for i in range(len(pots)):
    if pots[i] == '#':
        count += (i + start_count)

print('sum index of pots with plants: {}'.format(count))

