__author__ = 'carolynmcshea'
# Friday 22 May 2015
# an "m" Magazine FB Friendship Style Quiz


from graphnode import GraphNode


def parse_line(line):
    section_split = line.split("|")
    node_name = section_split[0].strip()
    adjacent_nodes = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_nodes:
        if a:
            adjacent.append(a.strip())
    text = section_split[2].strip()
    return node_name, adjacent, text


def load_story(filename):

    node_dict = {}
    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # this is a line in the correct format:
        if len(l.split("|")) == 3:
            node_name, adjacent_nodes, text = parse_line(l)
            # print "node " + node_name
            # print " adjacent:  " + str(adjacent_nodes)
            # print " text:  " + text

        node = GraphNode(node_name, adjacent_nodes, text)
        node_dict[node_name] = node

    file.close()

    return node_dict

story_dict = load_story("story.txt")


def play_game():

    start = story_dict["START"]

    while len(start.adjacent_nodes) > 0:

        print start.story_part

        input = raw_input()

        char_num = ord(input) - 97

        # using the character code as the index for the list
        # replacing the if statements by assigning a, b, and c the indicies 0, 1, and 2
        node_name = start.adjacent_nodes[char_num]
        next = story_dict[node_name]
        start = next

    print start

play_game()


