from datetime import datetime

start_time = datetime.now()
print('starting import at: \t\t{}'.format(start_time))

test = """
dabAcCaCBAcCcaDA
"""

# input = test.strip().split("\n")
# # turn the string into a list of characters
# input = list(input[0])

filename = "day5_input.txt"
input = list(open(filename).read())

def chain_react(input):
    # reaction = True
    i = 0
    while True:
        if (i % 100 == 0):
            print(".", end="")
        # print(i)
        if i + 1 >= len(input):
            # nothing more to compare
            break
        if ( ((input[i].isupper() and input[i+1].islower()) or (input[i].islower() and input[i+1].isupper())) and
             input[i].lower() == input[i+1].lower()):
            # print('different polarity')
            # print("comparing: '{}' to '{}'".format(input[i], input[i+1]))
            del input[i:i+2]
            # jump back ...
            if i - 1 >= 0:
                i = i - 1
            else:
                i = 0
        else:
            i = i + 1
    print()
    return(len(input))

orig_input = input.copy()
# print(orig_input)
print("chain length: {}".format(chain_react(input)))
# print(input)

print("part 2\n---")
from string import ascii_lowercase, ascii_uppercase

lowest = chain_react(input)

for upper, lower in zip(ascii_uppercase, ascii_lowercase):
    input_test = orig_input.copy()
    while upper in input_test:
        input_test.remove(upper)
    while lower in input_test:
        input_test.remove(lower)

    input_test_len = chain_react(input_test)
    print("removed: {}, {}  input_test_len: {}".format(upper, lower, input_test_len))

    if input_test_len < lowest:
        lowest = input_test_len

print("lowest: {}".format(lowest))

end_time = datetime.now()
print('finished import at: \t\t{}'.format(end_time))
print('total import time: \t\t{}'.format(end_time - start_time))
