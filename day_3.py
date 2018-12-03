import re

filename = "day3_input.txt"
input = open(filename).read().split("\n")

# test = """
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# """

# input = test.strip().split("\n")
# print(input)

fabric = [[0 for x in range(1000)] for x in range(1000)]

for line in input:
    data = re.split(r"^#(\d{1,})\s@\s(\d{1,})\,(\d{1,})\:\s(\d{1,})x(\d{1,})", line)
    # print(data)
    claim_id = int(data[1])
    start_x = int(data[2])
    start_y = int(data[3])
    len_x = int(data[4])
    len_y = int(data[5])

    for y in range(start_y, (start_y + len_y)):
        for x in range(start_x, (start_x + len_x)):
            if fabric[y][x] != 0:
                fabric[y][x] = "X"
            else:
                fabric[y][x] = claim_id

# count the "X" chars
count = 0
for y in range(len(fabric)):
    for x in range(len(fabric[y])):
        if fabric[y][x] == "X":
            count = count + 1

print (count)

# part 2
"""
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are
made.
"""
def intact():
    for line in input:
        data = re.split(r"^#(\d{1,})\s@\s(\d{1,})\,(\d{1,})\:\s(\d{1,})x(\d{1,})", line)
        # print(data)
        claim_id = int(data[1])
        start_x = int(data[2])
        start_y = int(data[3])
        len_x = int(data[4])
        len_y = int(data[5])

        intact = claim_id
        for y in range(start_y, (start_y + len_y)):
            for x in range(start_x, (start_x + len_x)):
                if fabric[y][x] != claim_id:
                    intact = None
        if intact == claim_id:
            return claim_id

print(intact())