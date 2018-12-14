import re
# import pdb
from collections import deque
from copy import deepcopy 
from itertools import cycle
from operator import itemgetter

# import numpy as np
# from sys import stdout; stdout.flush()

possible_carts = tuple(['<', '>', '^', 'v'])
possible_curves = tuple(['\\', '/']) # need to escape the backslash
horizontal  = tuple(['<', '>'])
vertical    = tuple(['^', 'v'])

cart = dict({
    'cart_name': '',
    'turns': cycle(['left', 'straight', 'right']),
    'pos_x': 0,
    'pos_y': 0,
    # possible directions (possible_carts) == '<', '>', '^', 'v'
    'direction': ''
})
carts = list()


def print_track(with_carts=False):
    temp_track_grid = deepcopy(track_grid)
    if with_carts:
        for cart in carts:
            temp_track_grid[cart['pos_y']][cart['pos_x']] = cart['direction']

    for y in range(len(track_grid)):
        for x in range(len(track_grid[y])):
            print(temp_track_grid[y][x], end='')
        print()


def move_cart(index):
    # print('moving cart: {}'.format(carts[index]))
    pos_y = carts[index]['pos_y']
    pos_x = carts[index]['pos_x']
    cur_direction = carts[index]['direction']
    next_pos_y = None
    next_pos_x = None
    next_direction = ''
    next_track = ''

    # create a copy of the track, and place the carts on it to detect colisions
    temp_track_grid = deepcopy(track_grid)
    for cart in carts:
            temp_track_grid[cart['pos_y']][cart['pos_x']] = cart['direction']

    # get next piece of track in 'front' of cart
    if cur_direction == '>':
        next_pos_x = pos_x + 1
        next_pos_y = pos_y
        next_track = track_grid[next_pos_y][next_pos_x]
    if cur_direction == '<':
        next_pos_x = pos_x - 1
        next_pos_y = pos_y
        next_track = track_grid[next_pos_y][next_pos_x]
    if cur_direction == '^':
        next_pos_x = pos_x
        next_pos_y = pos_y - 1
        next_track = track_grid[next_pos_y][next_pos_x]
    if cur_direction == 'v':
        next_pos_x = pos_x
        next_pos_y = pos_y + 1
        next_track = track_grid[next_pos_y][next_pos_x]
    # print('track in \'front\' of cart: {}'.format(next_track))

    # if the next track is a curve, turn the cart in the direction of the curve
    # below are the possible directions heading into the curve
    r"""
    /<->\
    ^   ^
    |   |
    v   v
    \<->/
    """
    if next_track in possible_curves:
        if cur_direction == '^' and next_track == '/':
            next_direction = '>'
        elif cur_direction == '^' and next_track == '\\':
            next_direction = '<'

        elif cur_direction == 'v' and next_track == '\\':
            next_direction = '>'
        elif cur_direction == 'v' and next_track == '/':
            next_direction = '<'

        elif cur_direction == '<' and next_track == '/':
            next_direction = 'v'
        elif cur_direction == '<' and next_track == '\\':
            next_direction = '^'

        elif cur_direction == '>' and next_track == '\\':
            next_direction = 'v'
        elif cur_direction == '>' and next_track == '/':
            next_direction = '^'
    elif next_track == '+':
        instruct = next(carts[index]['turns'])
        if cur_direction == '>' and instruct == 'right':
            next_direction = 'v'
        elif cur_direction == '>' and instruct == 'left':
            next_direction = '^'

        elif cur_direction == '<' and instruct == 'right':
            next_direction = '^'
        elif cur_direction == '<' and instruct == 'left':
            next_direction = 'v'

        elif cur_direction == '^' and instruct == 'right':
            next_direction = '>'
        elif cur_direction == '^' and instruct == 'left':
            next_direction = '<'
        
        elif cur_direction == 'v' and instruct == 'right':
            next_direction = '<'
        elif cur_direction == 'v' and instruct == 'left':
            next_direction = '>'
        else:
            next_direction = cur_direction
    # check if the temp_track_grid next track position has a cart ... colision!!
    elif temp_track_grid[next_pos_y][next_pos_x] in possible_carts:
        print('collision at (y, x): ({}, {})'.format(next_pos_y, next_pos_x))
        return False
        # next_pos_y, next_pos_x
    else:
        # track piece is a regular track ... '|' or '-'
        next_direction = cur_direction
    
    # print('next_pos_y: {}  next_pos_x: {}  next_direction: {}  next_track: {}'.format(next_pos_y, next_pos_x, next_direction, next_track))

    carts[index]['pos_y'] = next_pos_y
    carts[index]['pos_x'] = next_pos_x

    if next_direction == '':
        # next_direction = cur_direction
        from pdb import set_trace; set_trace()
    carts[index]['direction'] = next_direction

    # print('moved cart: {}'.format(carts[index]))

    return True




# On your initial map, the track under each cart is a straight path matching the
# direction the cart is facing.)

# Each time a cart has the option to turn (by arriving at any intersection), it
# turns left the first time, goes straight the second time, turns right the
# third time, and then repeats those directions starting again with left the
# fourth time, straight the fifth time, and so on. turns = cycle('left',
# 'straight', 'right')



# test track
# track = r"""
# /->-\        
# |   |  /----\
# | /-+--+-\  |
# | | |  | v  |
# \-+-/  \-+--/
#   \------/   
# """

# data track
from day13_input import track

print(track)

track_grid = list()

"""
this will take the carts off the track, and place them in the track list, and replace 
the track pieces with the correct direction track
"""
cart_name = 0
pos_y = 0
for line in track.strip().split('\n'):
    track_grid.append(list())
    pos_x = 0
    for piece in line:
        if piece in possible_carts:
            carts.append(deepcopy(cart))
            carts[-1]['cart_name'] = cart_name 
            carts[-1]['direction'] = piece
            carts[-1]['pos_x'] = pos_x
            carts[-1]['pos_y'] = pos_y
            if piece in vertical:
                piece = '|'
            elif piece in horizontal:
                piece = '-'
            cart_name += 1
        track_grid[-1].append(piece)
        pos_x += 1
    pos_y += 1

print('---')

print_track(with_carts=False)

print('---')

print_track(with_carts=True)

# loop until colision!

# sort the list first by the x_pos, and then by the y_pos.
# this SHOULD have the effect of ordering the list first 
# by y_pos, and then by x_pos
# https://stackoverflow.com/a/29849371/1445279
# items.sort(key=operator.itemgetter('age'), reverse=True)
carts.sort(key=itemgetter('pos_x'))
carts.sort(key=itemgetter('pos_y'))

# from pdb import set_trace; set_trace()

collision = False
while collision == False:
    for i in range(len(carts)):
        if move_cart(i) == False:
            collision = True
            break