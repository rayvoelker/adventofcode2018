import re
from copy import deepcopy

test = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

# input = list(test.strip().split("\n"))
# print(input)

filename = "day6_input.txt"
input = open(filename).read().split("\n")

def print_grid(target_grid):
    # print the grid
    for y in range(len(target_grid)):
        for x in range(len(target_grid[y])):
            print(target_grid[y][x], end=' ')
        print()


def tc_dist(cord1, cord2):
    distance = abs( int(cord1[0]) - int(cord2[0]) ) + abs( int(cord1[1]) - int(cord2[1]) )
    # print("distance between [{}, {}] and [{}, {}]: {}".format(cord1[0], cord1[1], cord2[0], cord2[1], distance))
    return(distance)


def get_closest(cord):
    # returns the closest coordinate from the coordinate list
    x = int(cord[0])
    y = int(cord[1])
    cord_value = grid[y][x]
    # record the distances
    distances = []

    if [cord[0], cord[1]] in coordinates:
        # print('coordinate is nearest to itself: {}'.format(cord_value))
        return cord_value
    else:
        # loop through the grid, find the coordinate value with the min distance
        min_dist = tc_dist(cord, coordinates[0])
        distances.append(min_dist)
        cord_value = 0
        # print("cord: {} test_distance: {}   min_dist: {}".format(0, min_dist, min_dist))

        for i in range(1, len(coordinates)):
            test_distance = tc_dist(cord, coordinates[i])
            distances.append(test_distance)
            if test_distance < min_dist:
                cord_value = i
                min_dist = test_distance
                
            # print("cord: {} test_distance: {}   min_dist: {}".format(i, test_distance, min_dist))

    if distances.count(min_dist) > 1:
        # print("distances: {}".format(distances))
        # can't call it for any cord, give it a '.'
        return '.'
    else:
        return cord_value

grid_max = 0
coordinates = []
for line in input:
    coordinates.append(re.compile(r"(\d*),\s(\d*)").split(line)[1:3])
    for value in coordinates[-1]:
        if int(value) > grid_max:
            grid_max = int(value)

# print(coordinates)
# print(grid_max + 1)

# create our grid
grid = [['-' for x in range(grid_max+1)] for x in range(grid_max+1)]

# place our items on the grid
for i in range(len(coordinates)):
    print(coordinates[i])
    x = int(coordinates[i][0])
    y = int(coordinates[i][1])
    grid[y][x] = i

# print the grid
# for y in range(len(grid)):
#     for x in range(len(grid[y])):
#         print(grid[y][x], end=' ')
#     print()

print()

# create a copy of the grid, where we will place our distances ...
dist_grid = deepcopy(grid)


# # tests
# print("---")
# print(get_closest(['3', '9']))

# print(get_closest(['8', '9']))

# print(tc_dist(['9', '9'], ['9', '9']))


# # fill in the closest point, given a grid number
for y in range(len(grid)):
    for x in range(len(grid[y])):
        str_x = str(x)
        str_y = str(y)
        dist_grid[y][x] = get_closest([str_x, str_y])

# print_grid(grid)
# print('---')
# print_grid(dist_grid)

edges = set()
# get list of edges
# there's probably a better way to do this ...
for y in range(len(dist_grid)):
    for x in range(len(dist_grid[y])):
        if y == 0 or y == len(dist_grid) - 1:
            edges.add(dist_grid[y][x])
        if x == 0 or x == len(dist_grid[y]) - 1:
            edges.add(dist_grid[y][x])

print('edges: {}'.format(edges))

# get the area of each cord that's finite
max_area = 0
for i in range(len(coordinates)):
    if i in edges:
        # coordinate is infinite, don't count it...
        pass
    else:
        count = 0
        for y in range(len(dist_grid)):
            count = count + dist_grid[y].count(i)
        if count > max_area:
            max_area = count
        print("count for coordinate {}: {}".format(i, count))

print(max_area)
print("done.")