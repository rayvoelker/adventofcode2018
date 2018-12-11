import re
import numpy
from PIL import Image

test = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""

point_node = dict({
    'pos_x' : 0,
    'pos_y' : 0,
    'v_x'   : 0,
    'v_y'   : 0
})

point_nodes = list()

# input = test.strip().split('\n')

filename = "day10_input.txt"
input = open(filename).read().strip().split("\n")

for line in input:
    digits = [int(d) for d in re.findall(r'-?\d+', line)]
    # print(digits)
    point_nodes.append(point_node.copy())
    point_nodes[-1]['pos_x'] = digits[0]
    point_nodes[-1]['pos_y'] = digits[1]
    point_nodes[-1]['v_x'] = digits[2]
    point_nodes[-1]['v_y'] = digits[3]

# for node in point_nodes:
#     print(node)

# x_cords = [x['pos_x'] for x in point_nodes]
# y_cords = [y['pos_y'] for y in point_nodes]
# x_vs = [x['v_x'] for x in point_nodes]
# y_vs = [y['v_y'] for y in point_nodes]
size_x = list()
size_y = list()
area = list()

# find the smallest box drawn given the movement of the nodes, with a big guess for the range
for i in range(10088):
    x_temp = []
    y_temp = []
    for node in point_nodes:
        x_temp.append(node['pos_x'] + (i * node['v_x']))
        y_temp.append(node['pos_y'] + (i * node['v_y']))
    size_x.append(max(x_temp) - min(x_temp))
    size_y.append(max(y_temp) - min(y_temp))
    area.append(size_x[-1] * size_y[-1])


print('min area: {}'.format(min(area)))
min_area_index = area.index(min(area))

print('min area at count: {}'.format(min_area_index))

# draw it!

x_temp = list()
y_temp = list()
for node in point_nodes:
        x_temp.append(node['pos_x'] + (min_area_index * node['v_x']))
        y_temp.append(node['pos_y'] + (min_area_index * node['v_y']))

print('x_temp: {}'.format(x_temp))
print('y_temp: {}'.format(y_temp))

print('max(x_temp): {}'.format(max(x_temp)))
print('max(y_temp): {}'.format(max(y_temp)))

print('min(x_temp): {}'.format(min(x_temp)))
print('min(y_temp): {}'.format(min(y_temp)))

data = numpy.zeros((max(y_temp) + 1, max(x_temp) + 1, 3), dtype=numpy.uint8)

for x, y in zip(x_temp, y_temp):
    data[y][x] = [255, 255, 255]

image = Image.fromarray(data)
image.save('day10.png')
image.show()