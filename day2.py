"""
To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare it
to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, 
and three of them contain a letter which appears exactly three times. 
Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""

# # test input
# test = """
# abcdef
# bababc
# abbcde
# abcccd
# aabcdd
# abcdee
# ababab
# """
# # input = input.strip()
# input = test.strip().split("\n")

# open the input file
filename = "day2_input.txt"
input = open(filename).read().split("\n")

print(input)

appear_2x = 0
appear_3x = 0
for line in input:
    # sort the string so we can iterate through it and count letters appearing
    sorted_line = ''.join(sorted(line))
    print("line: {} sorted_line: {}".format(line, sorted_line))

    # start by taking the first character, count it remove all occurances from string, until no more string
    i = 0
    has_appear_2x = False
    has_appear_3x = False

    while i < len(sorted_line):
        print("{}:  count: {}".format(sorted_line[i], sorted_line.count(sorted_line[i])))
        if sorted_line.count(sorted_line[i]) == 2:
            has_appear_2x = True
        if sorted_line.count(sorted_line[i]) == 3:
            has_appear_3x = True
        
        i = i + sorted_line.count(sorted_line[i])

    if has_appear_2x:
        appear_2x = appear_2x + 1
    if has_appear_3x:
        appear_3x = appear_3x + 1

print("appear_2x: {}".format(appear_2x))
print("appear_3x: {}".format(appear_3x))
print("checksum: {}".format(appear_2x * appear_3x))



# part 2
"""
The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the second
and fourth). However, the IDs fghij and fguij differ by exactly one character,
the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above,
this is found by removing the differing character from either ID, producing
fgij.)
"""

# test = """
# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# """
# input = test.strip().split("\n")


found_one = None
found_two = None

for line in input:
    for compare_line in input:
        if line == compare_line:
            # this is the same line ... skip it
            pass
        else:
            # print("line: {} compare_line: {}".format(line, compare_line))
            # compare each character, and if we differ by more than 1, stop comparing
            differ = 0
            for i in range(len(line)):
                if line[i] != compare_line[i]:
                    differ = differ + 1
                if differ > 1:
                    break
            if differ == 1:
                found_one = line
                found_two = compare_line
                break

print("found_one: {}\nfound_two: {}".format(found_one, found_two))
