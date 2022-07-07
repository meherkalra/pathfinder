# Author: Meher Kalra
# Date: 10 March 2022
# Purpose: to write the code to plot vertices on the map_img

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

# initializing variables
mpressed = False
x1 = None
x2 = None
start = None
goal = None

# initializing constants
IMG_WIDTH = 1012
IMG_HEIGHT = 811
map_img = load_image("dartmouth_map.png")

# key press functions that record when a key is pressed, released and moves
def mpress(mx, my):
    global mpressed
    mpressed = True

def mmove(mx, my):
    global x1, x2
    x1 = mx
    x2 = my

def mrelease(mx, my):
    global mpressed
    mpressed = False

vertex_dictionary = load_graph("dartmouth_graph.txt")

# initializing a draw function that draws the vertices on the map
def draw():
    global start, goal, x1, x2

    draw_image(map_img, 0, 0)

    for vert in vertex_dictionary:
        if start == True:
            start.draw_vertex(1, 0.2, 0)
        if goal == True:
            goal.draw_vertex(1, 0.2, 0)
        if mpressed and vertex_dictionary[vert].mouse_vert(x1, x2):
            start = vertex_dictionary[vert]
        if start and not mpressed and vertex_dictionary[vert].mouse_vert(x1, x2):
            goal = vertex_dictionary[vert]

        vertex_dictionary[vert].draw_vertex(0, 0.2, 1)

        if vertex_dictionary[vert].adjacency_list:
            vertex_dictionary[vert].draw_all_edges(0, 0, 1)

        if start and goal and start != goal:
            path = bfs(vertex_dictionary[start.name], vertex_dictionary[goal.name])
            for i in range(len(path)-1):
                path[i].draw_edges(1, 0.2, 0, path[i + 1])
                path[i].draw_vertex(1, 0.2, 0)

start_graphics(draw, width=IMG_WIDTH, height=IMG_HEIGHT, mouse_press=mpress, mouse_release=mrelease, mouse_move=mmove)



