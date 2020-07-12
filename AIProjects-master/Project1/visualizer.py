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
    shape = (101,101)
    nvis = np.random.choice([0,1], size=shape, p=[.70,.30])
    #nvis = [[None for x in range(101)]for y in range(101)]
    #initialize initial grid graph
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            nvis[i][s] = int(line[s*2:s*2+2].rstrip())

    #out.readline() #dump grid data
    startStr = out.readline()
    goalStr = out.readline()
    start_list = startStr.split()
    goal_list = goalStr.split()
    node = out.readline()
    while not node.startswith('target reached'):
        node_list = node.split()
        if nvis[int(node_list[2].rstrip())][int(node_list[1])] != 1:
            nvis[int(node_list[2].rstrip())][int(node_list[1])] = (int(node_list[0]) % 5+2)
        node = out.readline()
    nvis[int(start_list[4])][int(start_list[2])] = 7
    nvis[int(goal_list[4])][int(goal_list[2])] = 7
    out =np.asarray(nvis)
    plt.imshow(nvis,vmin = 0, vmax = len(cmap.colors),cmap=cmap,interpolation='nearest',aspect='equal')
    #plt.xticks([]), plt.yticks([])
    plt.autoscale()
    plt.savefig("vis.png",bbox_inches="tight")
    plt.show()
    plt.figure()


if __name__ == "__main__":
    if os.path.exists("vis.png"):
        os.remove("vis.png")
    output = open("output.txt")
    other = output.readline().strip()
    grid = open(other)
    visualizer(output, grid)
    output.close()
    grid.close()
