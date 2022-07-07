# Author: Meher Kalra
# Date: 6 March 2022
# Purpose: LAB4- To write the vertex class

from cs1lib import *

#radius of circle
RADIUS = 10

# to write a Vertex class
class Vertex:
    # instance variables: name, x, y
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = []

    def __str__(self):
        str1 = ""
        for i in self.adjacency_list[:-1]:
            str1 = str1 + self.name + ","
        str1 = str1 + self.adjacency_list[-1].name
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent Vertices: " + str1

# initializing draw functions to draw vertices on maps
    def draw_vertex(self, r, g, b):
        set_stroke_width(3)
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

# initializing draw functions to draw the edges on maps
    def draw_edges(self, r, g, b, other_vertex):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

# initializing draw functions to draw all the edges on maps
    def draw_all_edges(self, r, g, b):
        for vertex in self.adjacency_list:
            self.draw_edges(r, g, b, vertex)

# changes the color when the mouse is on the vertex
    def mouse_vert(self, mx, my):
        return self.x - RADIUS <= mx <= self.x + RADIUS and self.y - RADIUS <= my <= self.y + RADIUS

#
# # lab4_checkpoint.py
# # CS 1 Lab Assignment #4 checkpoint by THC.
# # Creates a dictionary of Vertex objects based on reading in a file.
# # Writes out a string for each Vertex object to a file.
#
# from load_graph import load_graph
#
# vertex_dictionary = load_graph("dartmouth_graph.txt")
#
# out_file = open("vertices.txt", "w")
# for vertex in vertex_dictionary:
#     out_file.write(str(vertex_dictionary[vertex]) + "\n")
# out_file.close()