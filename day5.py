# get ready to heat up your room with how in inefficient this is!

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

def react(temp_input):
    for i in range(len(temp_input) - 1):
        # print("comparing: '{}' to '{}'".format(temp_input[i], temp_input[i+1]))
        if ( (temp_input[i].isupper() and temp_input[i+1].islower()) or (temp_input[i].islower() and temp_input[i+1].isupper()) ):
            # characters are different polarity, check them if they're the same letter
            # print('diff polarity')
            if temp_input[i].lower() == temp_input[i+1].lower():
                # print('reacting...')
                del temp_input[i:i+2]
                return()
    return()


print(input)
count_reaction = 0
while True:
    temp_input = input.copy()
    react(temp_input)
    if len(input) == len(temp_input):
        # no reaction was found, break
        print("no reaction ... ")
        break
    else:
        count_reaction = count_reaction + 1
        # del input[:]
        input = temp_input.copy()
    # print(input)

print(count_reaction)
print(input)

print("length remaining: {}".format(len(input)))

end_time = datetime.now()
print('finished import at: \t\t{}'.format(end_time))
print('total import time: \t\t{}'.format(end_time - start_time)) 

# part 2

"""
What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
"""

from string import ascii_lowercase, ascii_uppercase

shortest = len(input)



def collapse_len(input):
    collapse_input = input.copy()
    while True:
        temp_input = collapse_input.copy()
        react(temp_input)
        if len(collapse_input) == len(temp_input):
            # no reaction was found, break
            print("no reaction ... ")
            break
        else:
            # del input[:]
            collapse_input = temp_input.copy()
        # print(input)
    length = len(collapse_input)
    return(length)

# re-read the input and create a copy of the original ...

# input_orig = test.strip().split("\n")
# # turn the string into a list of characters
# input_orig = list(input_orig[0])

filename = "day5_input.txt"
input_orig = list(open(filename).read())

# print(input_orig)

for upper, lower in zip(ascii_uppercase, ascii_lowercase):
    input_test = input_orig.copy()
    while upper in input_test:
        input_test.remove(upper)
    while lower in input_test:
        input_test.remove(lower)

    test_length = collapse_len(input_test)
    if test_length < shortest:
        shortest = test_length

    print("{}, {} removed: ".format(upper, lower))
    # print(input_test)
    print("length: {}".format(test_length))
    print()

print("shortest: {}".format(shortest))