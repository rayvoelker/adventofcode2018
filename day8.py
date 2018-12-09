import re
from copy import deepcopy

def print_nodelist():
    print('---')
    for i in range(len(nodelist)):
        print(nodelist[i])
    print('---')

"""
A header, which is always exactly two numbers:
    The quantity of child nodes.
    The quantity of metadata entries.
    
Zero or more child nodes (as specified in the header).
One or more metadata entries (as specified in the header).
"""

# the orig test set
# test = """
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# """
# input = list(test.strip().split(' '))

filename = "day8_input.txt"
input = open(filename).read().strip().split(" ")

node = {
    "num_child_nodes": 0,
    "num_metadata_entries": 0,
    "metadata_entries": [],
    "child_nodes": []
}

nodelist = list()

def create_node():
    
    # read the header info
    try:
        num_child_nodes = int(input.pop(0))
        num_metadata_entries = int(input.pop(0))
    except:
        # no more to pop! .. this sholdn't happen
        return None

    nodelist.append(deepcopy(node))
    list_node = nodelist[-1]

    list_node['num_child_nodes'] = num_child_nodes
    list_node['num_metadata_entries'] = num_metadata_entries

    # return the index of the last node inserted
    return len(nodelist) - 1


def add_metadata(node_number, num_metadata_entries, child_nodes):
    for i in range(num_metadata_entries):
        nodelist[node_number]['metadata_entries'].append(int(input.pop(0)))
    nodelist[node_number]['child_nodes'] = child_nodes.copy()


def loop_for_children(node_number):
    print("looping for children of node: {}".format(node_number))
    num_child_nodes = nodelist[node_number]['num_child_nodes']
    num_metadata_entries = nodelist[node_number]['num_metadata_entries']
    print("num children: {}".format(num_child_nodes))
    print("num metadata_entries: {}".format(num_metadata_entries))

    child_nodes = list()
    for i in range(num_child_nodes):
        child_nodes.append(create_node())
        loop_for_children(child_nodes[-1])

    add_metadata(node_number, num_metadata_entries, child_nodes)


print(input)

# create and add the first node
root = create_node()

# hold onto your butts ... it's getting recursive in here
loop_for_children(root)

print(input)
print_nodelist()

# add metadata entries
total = 0
for i in range(len(nodelist)):
    for j in range(len(nodelist[i]['metadata_entries'])):
        total = total + int(nodelist[i]['metadata_entries'][j])

print("total: {}".format(total))