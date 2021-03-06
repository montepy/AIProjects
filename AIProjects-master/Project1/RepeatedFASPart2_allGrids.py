
import math
import BreakLargeHeap
import BreakSmallHeap
import GridNode
import random
import sys
import os
from time import time

DEBUGFLAG = False

def ComputePath(rgrid, goal, openlist, closedlist, counter):
    #loggrid = [101][101]
    #TODO finish implementing A* later.

    acounter = 0
    while goal.costToGo > openlist.getMin().fvalue() and openlist.size != 500:  #while smallest f-value less than goal g value
        #basically, while goal has not been reached, or fvalue() is greater than infinity, indicating a blocked path
        #take smallest node and expand
        node = openlist.removeMin()

        acounter += 1
        if DEBUGFLAG:
            print("computePath iteration#", acounter)
            print("expanding - ")
            print("\texpanding node at :  ( " + str(node.x), ',', str(node.y), ')')
            print("\tfvalue - ", node.fvalue(), "\n\tcostToCome - ", node.costToCome, "\n\tcostToGo - ", node.costToGo, "\n\tblocked - ", node.blocked,  '\n')
            print("openlist size = ", openlist.size, "\nclosedlist size = ", len(closedlist),"\n")

        #TODO need to check if this current element is in the closed list and to throw it away if it is
        actions_possible = node.expand(openlist, closedlist, rgrid)
        #commenting for now
        #print("\nexpanding node at :  ( " + str(node.x), ',', str(node.y), ')')
        #print("\tfvalue - ", node.fvalue(), "\n\tcostToCome - ", node.costToCome, "\n\tcostToGo - ", node.costToGo, "\n\tblocked - ", node.blocked,  '\n')
        #print("openlist size = ", openlist.size, "\nclosedlist size = ", len(closedlist),"\n")
        closedlist.append(node)
        for subnode in actions_possible:
            action_cost = 1
            if closedlist.count(subnode):
                continue
            #if subnode.blocked:
                #continue
            #subnode.setCostToCome(goal.x, goal.y)
            #if node.action_cost == math.inf and node.blocked:
                #closedlist.append(node)
                #continue
            if subnode.search < counter:
                #if search value(last time encountered) is less than counter, set search to counter and
                #set g value to infinity to ensure next if statement triggers
                subnode.costToGo = math.inf
                subnode.search = counter
            if subnode.costToGo > (node.costToGo + action_cost):  #should be 1 for cost of moving to node, right?
                #sets subnode g value appropriately and establishes tree
                subnode.costToGo = node.costToGo + subnode.action_cost
                subnode.parent = node
                #update subnode values if the node was in the openlist
                ind = openlist.check(subnode)
                subnode.setCostToCome(goal.x, goal.y)
                if ind != -1:
                    openlist.delete(ind)
                openlist.insert(subnode)
        actions_possible = []

def main(wfile,firstRun,gridf,rgrid,startgoalCollection):
    f = None
    if DEBUGFLAG:
        import pdb;pdb.set_trace()
    else:
        #pass
        if os.path.exists(wfile):
            os.remove(wfile)
        old_stdout = sys.stdout
        f = open(wfile,'w')
        sys.stdout = f
        #sys.stdout = open(wfile,'w')
    start_time = time()
    expanded = 0
    counter = 0  #set iteration counter
    text = gridf
    #grid = open(text)
    print(text)

    """ commenting out this block becuase I want to make this outside of main
    rgrid = [[None for x in range(101)]for y in range(101)]
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            rgrid[i][s] = GridNode.node(i, s, math.inf, None, 0, line[s*2:s*2+2].rstrip() == "1")
            #(x, y, costToGo, parent, search, blocked)

    """
    #lstart, lgoal, start, goal = getRandomSG(rgrid)

    lstart, lgoal, start, goal = startgoalCollection

    print("start: (", start[0], ',', start[1],")")
    print("goal: (", goal[0], ',', goal[1],")")
    lstart.setCostToCome(goal[0], goal[1])
    lstart.costToGo = 0

    if firstRun:
        openlist = BreakLargeHeap.BLHeap()
    else:
        openlist = BreakSmallHeap.BSHeap()

    closedlist = []

    while lstart != lgoal:
        lgoal.costToGo = math.inf
        #increment counter to keep track of nodes over iterations
        counter = counter+1
        #initialize lists
        openlist.wipe()
        closedlist = [] #make array for now. #TODO make closed list consistent over code
        openlist.insert(lstart)
        #run A*
        ComputePath(rgrid, lgoal, openlist, closedlist, counter)
        expanded += len(closedlist)
        #if openlist.size == 0 or openlist.size > 500 or len(closedlist)> 2500 or time() - start_time > 10*10*10*10:
        if openlist.size == 0 or time() - start_time > 5:
            print("Cannot reach target")
            print("num-expanded:" + str(expanded))
            print("counter:" + str(counter))
            #print("path_length:" + str(len(path)))
            print("start: (", start[0], ',', start[1],")")
            print("goal: (", goal[0], ',', goal[1],")")
            print("execution_time:",str(time()-start_time))
            return
        path = []
        #TODO move along path and implement action-cost adjustments
        #need to have ability to track changes over the path and iterate until action changes
        #node = lgoal
        node = openlist.getMin()
        while node != lstart:
            path.append(node)
            node = node.parent #why
            #if node is lstart:
                #break
        path.append(lstart)
        nstart = None
        flagnode = None
        for i in range(len(path),0,-1):
            #TODO implement later.
            check = path[i-1]
            print(str(counter),check.x,check.y,str(check.blocked))
            if check == goal:
                nstart = check
                break
            if check.blocked:
                flagnode = check
                break
            #i -= 1
            nstart = check
            #check = path[len(path)-1-i]
        lstart = nstart
        if flagnode is not None:
            flagnode.action_cost = math.inf
    print("target reached")
    print("num-expanded:" + str(expanded))
    print("counter:" + str(counter))
    print("path_length:" + str(len(path)))
    print("start: (", start[0], ',', start[1],")")
    print("goal: (", goal[0], ',', goal[1],")")
    print("execution_time:",str(time()-start_time))

    if f != None:
        sys.stdout = old_stdout #https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
        f.close()
    return

def getRandomSG(rgrid):
    lstart = lgoal = start = goal = None
    while (lstart is None) or (lgoal is None) or lstart.blocked or lgoal.blocked:
        #goal = ( 0 , 0 )
        #start = ( 98 , 100 )
        goal = (random.randint(0,100),random.randint(0,100)) # tuple(column, row)
        start = (random.randint(0,100),random.randint(0,100)) # tuple(column, row)
        #using random gen for the moment
        #initialize start and goal nodes
        lstart = rgrid[start[0]][start[1]]
        lgoal = rgrid[goal[0]][goal[1]]

    return lstart, lgoal, start, goal

def makergrid(gridf):
    grid = open(gridf)
    rgrid = [[None for x in range(101)]for y in range(101)]
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            rgrid[i][s] = GridNode.node(i, s, math.inf, None, 0, line[s*2:s*2+2].rstrip() == "1")
            #(x, y, costToGo, parent, search, blocked)
    return rgrid

def printNodeList(closedlist):
    count = 1
    for node in closedlist:
        print("Element#", count,'\t', node," : fvalue - ", node.fvalue(), " , CostToGo - ", node.costToGo)
        count +=1

def argv1Check():
    if len(sys.argv) <= 1:
        print("Please Input a Grid File from the arrs/randGrid folder")
        exit()

def listOfGridFiles():
    gridflist = []
    for i in range(10):
        gridflist.append('0' + str(i) + '.txt')

    for i in range(41):
        gridflist.append(str(i+10)+'.txt')

    #print(gridflist)
    #exit()
    return gridflist

if __name__ == "__main__":
    argv1Check()
    gridflist = listOfGridFiles()

    for i in range(20):
        print("Running Grid - ", i)
        currentGrid = gridflist[i]
        gridf = sys.argv[1] + "\\" + currentGrid
        writef = sys.argv[2] + "\\C" + currentGrid
        rgrid = makergrid(gridf)
        startgoalCollection = getRandomSG(rgrid)
        main(writef, True, gridf, rgrid, startgoalCollection)
        print("Finished search with larger G value.")


        rgrid = []#Im sorry if this is a big memory leak this is my first time programing in python

        rgrid = makergrid(gridf)
        lstart, lgoal, start, goal = startgoalCollection
        lstart = rgrid[start[0]][start[1]]
        lgoal = rgrid[goal[0]][goal[1]]
        startgoalCollection = lstart, lgoal, start, goal#doing this because I am afraid that many of the nodes have already been set in the previous run

        writef = sys.argv[2] + "\\D" + currentGrid
        main(writef, False, gridf, rgrid, startgoalCollection)#false is for second runthrough with minimum G value dominating
        print("Finished search with smaller G value.")
