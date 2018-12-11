import numpy
import pdb

# constants for our power grid
serial_number = 9995
x_size = 300
y_size = 300

def get_rack_id(x):
    return x + 10

def get_begin_power_level(rack_id, y):
    return int(rack_id * y)

def increase_power_level(power_level):
    return power_level + serial_number

# Set the power level to itself multiplied by the rack ID.
def multiply_power(power_level, rack_id):
    return int(power_level * rack_id)

def hundreds(power_level):
    return (power_level // 100) % 10

# Subtract 5 from the power level.
def sub_5(power_level):
    return (power_level - 5)

def corner_sum(y, x, square_size=3):
    # print('y: {}    x: {}'.format(y, x))
    grid_slice_sum = 0
    try:
        grid_slice = grid_powers[y:(y+square_size), x:(x+square_size)]
        # print(grid_slice)
        grid_slice_sum = grid_slice.sum()
    except:
        print('out of range?')

    # print('grid_slice shape: {}'.format(grid_slice.shape))
    y_shape, x_shape = grid_slice.shape
    if y_shape == square_size and x_shape == square_size:
        return grid_slice_sum
    else:
        return 0

grid_powers = numpy.zeros((y_size, x_size), dtype=int)

# grid is called (X,Y) in our challenge, but accessed, (y-1, x-1) in our local grid
# top-right cell is (300,1) = 1 ...
# x = 300
# y = 1
# grid_powers[(y-1), (x-1)] = 1
# print(grid_powers)
# print('grid_powers.shape: {}'.format(grid_powers.shape))
# print('---')
# grid_powers[(y-1)+1, (x-1)] = 1
# print(grid_powers)
# print('grid_powers.shape: {}'.format(grid_powers.shape))
# print('---')
# 


for y in range(y_size):
    for x in range(x_size):
        # start computing the fuel cell's power level
        # print('---')
        # print('x, y: {}, {}'.format(x+1, y+1))
        rack_id = get_rack_id(x+1)
        # print('rack_id: {}'.format(rack_id))
        begin_power_level = get_begin_power_level(rack_id, y+1)
        # print('begin_power_level: {}'.format(begin_power_level))
        power_level = increase_power_level(begin_power_level)
        # print('power_level: {}'.format(power_level))
        power_level = multiply_power(power_level, rack_id)
        # print('power_level: {}'.format(power_level))
        power_level = hundreds(power_level)
        # print('power_level: {}'.format(power_level))
        power_level = sub_5(power_level)
        # print('power_level: {}'.format(power_level))
        # print('---')
        # print()

        # print('grid_powers[{}, {}] x,y ({},{}) = {}'.format(y, x, x, y, power_level))
        grid_powers[y, x] = power_level

dial_max = 0
dial_max_pos = 0
dial_max_x_pos = 0
dial_max_y_pos = 0

for dial in range(300 + 1):
    # pdb.set_trace()
    # build the grid with the corner sums computed
    grid_corner_sums = numpy.zeros((y_size, x_size), dtype=int)

    max = 0
    max_x = 0
    max_y = 0
    for y in range(y_size):
        for x in range(x_size):
            c_sum = corner_sum(y, x, dial)
            if c_sum >= max:
                max = c_sum
                max_x = x
                max_y = y
            grid_corner_sums[y, x] = c_sum

    print('dial: {} max: {}  x,y: {},{}'.format(dial, max, max_x+1, max_y+1))

    if max > dial_max:
        dial_max = max
        dial_max_pos = dial
        dial_max_x_pos = max_x
        dial_max_y_pos = max_y

print('dial_max: {} dial_max_pos: {}    x,y: {},{}'.format(dial_max, dial_max_pos, dial_max_x_pos+1, dial_max_y_pos+1 ))