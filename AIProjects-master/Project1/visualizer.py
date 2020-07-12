import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import fileinput
import os

def visualizer(out, grid):
    colDict = {
        0:'w',
        1:'k',
        2:'b',
        3:'g',
        4:'r',
        5:'c',
        6:'m',
        7:'y'
    }
    cmap = colors.ListedColormap(['white','black','blue','green','red','cyan','magenta','yellow'])
    #initialize grid
    nvis = [[None for x in range(101)]for y in range(101)]
    #initialize initial grid graph
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            nvis[i][s] = int(line[s:s+2].rstrip())
    #out.readline() #dump grid data
    startStr = out.readline()
    goalStr = out.readline()
    start_list = startStr.split()
    goal_list = goalStr.split()
    nvis[int(start_list[2])][int(start_list[4])] = 7
    nvis[int(goal_list[2])][int(goal_list[4])] = 7
    node = out.readline()
    while not node.startswith('target reached'):
        node_list = node.split()
        if nvis[int(node_list[1])][int(node_list[2].rstrip())] != 1:
            nvis[int(node_list[1])][int(node_list[2].rstrip())] = (int(node_list[0]) % 5+2)
        node = out.readline()
    plt.figure()
    plt.imshow(nvis,vmin = 0, vmax = len(cmap.colors),cmap=cmap,interpolation='nearest')
    plt.tight_layout()
    plt.xticks([]), plt.yticks([])
    plt.show()
    plt.savefig("Project1\vis.png")


if __name__ == "__main__":
    if os.path.exists("vis.png"):
        os.remove("vis.png")
    output = open("output.txt")
    other = output.readline().strip()
    grid = open(other)
    visualizer(output, grid)
