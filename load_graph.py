# Author: Meher Kalra
# Date: 6 March 2022
# Purpose: Parse through text file to create vertex objects and add to the dictionary

from vertex import Vertex

# Defining a function load_graph which creates one Vertex object per line in the data file
# and adds to the dictionary a reference to each Vertex object it creates
def load_graph(file_data):
    vert_dict = {}

    file = open(file_data, "r")

    for line in file:
        split = line.split(";")
        name = split[0].strip()
        x = int(split[2].split(",")[0].strip())
        y = int(split[2].split(",")[1].strip())
        vertex = Vertex(name, x, y)
        vert_dict[name] = vertex

    file.close()
    file = open(file_data, "r")

    for line in file:
        split = line.split(";")
        name = split[0].strip()
        adjacency_list = split[1].strip().split(",")

        for i in adjacency_list:
            if i:
                vert_dict[name].adjacency_list.append(vert_dict[i.strip()])

    file.close()
    return vert_dict
