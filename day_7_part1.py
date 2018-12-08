import re

def not_current_requirement(step):
    if not any(inst['step'] == step for inst in instructions):
        return True
    else:
        return False

def remove_step(step):
    print('removing: {}'.format(step))
    for i in range(len(instructions)):
        # print('@@')
        # print(instructions[i]['step'], instructions[i]['requires'])
        # print('@@')
        if instructions[i]['requires'] == step:
            instructions[i]['step'] = '-'
            instructions[i]['requires'] = '-'
    try:
        possible_steps.remove(step)
    except:
        print('step: {} not removed'.format(step))

def log():
    print('---')
    print("instructions: ")
    for line in instructions:
        print(line)
    print("possible_steps: ")
    print(possible_steps)
    print("available_steps: ")
    print(available_steps)
    print("taken_steps: ")
    print(taken_steps)
    print('---')


test = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""

# input = list(test.strip().split("\n"))
# print(input)

filename = "day7_input.txt"
input = open(filename).read().split("\n")

print(input)

# list of dicts that look like this ... {'step': 'A', 'requires': 'H'}
instructions = list()
possible_steps = set()
available_steps = list()
taken_steps = list()

# build our instructions
for line in input:
    print(line)
    temp = re.split(r"^Step\s([A-Z]).*step\s([A-Z]).*", line)
    print(temp)
    detail = {'step': temp[2], 'requires': temp[1]}
    instructions.append(detail)
    possible_steps.add(temp[1])
    possible_steps.add(temp[2])

log()

count = 0
while len(possible_steps):
    # print('count: {}'.format(count))
    # if count > 2:
    #     break
    for step in possible_steps:
        # check to see if the step is a CURRENT requirement
        if not_current_requirement(step):
            available_steps.append(step)

    available_steps.sort(reverse=True)

    current_step = available_steps.pop()
    remove_step(current_step)
    taken_steps.append(current_step)

    while len(available_steps):
        possible_steps.add(available_steps.pop())

    log()

    count += 1

for step in taken_steps:
    print(step, end='')

print()