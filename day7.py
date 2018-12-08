import re
from string import ascii_uppercase
import pdb

letters = list(ascii_uppercase)
letters.insert(0, '-')
print(letters)
print("index of z: {}".format(letters.index('Z')))

def worker_available():
    for i in range(len(workers)):
        if workers[i]['working_on'] == None:
            return i
    
    return False

def work_it():
    for i in range(len(workers)):
        if workers[i]['working_on']:
            workers[i]['seconds_left'] = workers[i]['seconds_left'] - 1

            if workers[i]['seconds_left'] == 0:
                remove_step(workers[i]['working_on'])
                taken_steps.append(workers[i]['working_on'])
                workers[i]['working_on'] = None

def not_current_requirement(step):
    if not any(inst['step'] == step for inst in instructions):
        return True
    else:
        return False

def remove_step(step):
    # print('removing: {}'.format(step))
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
        pass
        # print('step: {} not removed'.format(step))

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

input = list(test.strip().split("\n"))
print(input)

# filename = "day7_input.txt"
# input = open(filename).read().split("\n")

print(input)

# list of dicts that look like this ... {'step': 'A', 'requires': 'H'}
instructions = list()
possible_steps = set()
available_steps = list()
taken_steps = list()
seen_multiple = set()

# build our instructions
for line in input:
    print(line)
    temp = re.split(r"^Step\s([A-Z]).*step\s([A-Z]).*", line)
    print(temp)
    detail = {'step': temp[2], 'requires': temp[1]}
    instructions.append(detail)
    possible_steps.add(temp[1])
    possible_steps.add(temp[2])

# log()

workers = [
    {'working_on': None, 'seconds_left': 0}
]



count = 0
while len(possible_steps):
    count = count + 1
    # print('count: {}'.format(count))
    # if count > 2:
    #     break

    

    for step in possible_steps:
        # check to see if the step is a CURRENT requirement
        if not_current_requirement(step):
            print('adding step ...')
            available_steps.append(step)

    available_steps.sort(reverse=True)

    log()

    print("{}:  length available_steps: {}".format(count, len(available_steps)))
    if len(available_steps) > 1:
        print("available_steps: {}".format(available_steps))
        for item in available_steps:
            seen_multiple.add(item)

    # DO WORK HERE ---

    for i in range(len(available_steps)):
        worker = worker_available()
        if worker != None:
            print("worker: {}".format(worker))
            workers[worker]['working_on'] = available_steps.pop()
            workers[worker]['seconds_left'] = 1

    # decrement all the workers remaining time to work, etc
    work_it()

    # print('worker 1')
    # current_step = available_steps.pop()
    # remove_step(current_step)
    # taken_steps.append(current_step)

    # # second worker can do this ... if available
    # if len(available_steps):
    #     print('worker 2!')
    #     current_step = available_steps.pop()
    #     remove_step(current_step)
    #     taken_steps.append(current_step)

    # --- WORK STOPS HERE

    # throw the rest back into the possible steps ... couldn't do them
    while len(available_steps):
        possible_steps.add(available_steps.pop())

    # log()

for step in taken_steps:
    print(step, end='')

print()