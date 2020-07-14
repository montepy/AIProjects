
import math
import BreakLargeHeap
import GridNode
import random
import sys
from time import time

DEBUGFLAG = False

def ComputePath(rgrid, goal, openlist, closedlist, counter, sgoal):
    #loggrid = [101][101]
    #TODO finish implementing A* later.
    acounter = 0
    while goal.costToGo > openlist.getMin().fvalue():  #while smallest f-value less than goal g value
        acounter += 1
        #basically, while goal has not been reached, or fvalue() is greater than infinity, indicating a blocked path
        #take smallest node and expand
        node = openlist.removeMin()
        #TODO need to check if this current element is in the closed list and to throw it away if it is
        if DEBUGFLAG:
            print("computePath iteration#", acounter)
            print("expanding - ")

        actions_possible = node.expand(openlist, closedlist, rgrid)
        #commenting for now
        if DEBUGFLAG:
            print("\texpanding node at :  ( " + str(node.x), ',', str(node.y), ')')
            print("\tfvalue - ", node.fvalue(), "\n\tcostToCome - ", node.costToCome, "\n\tcostToGo - ", node.costToGo, "\n\tblocked - ", node.blocked,  '\n')
            print("openlist size = ", openlist.size, "\nclosedlist size = ", len(closedlist),"\n")

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
                if subnode.search != counter and subnode.search != 0:
                    if subnode.fvalue() < sgoal:
                        subnode.setCostToCome(sgoal-subnode.costToGo)
                    #subnode.setCostToCome(subnode.costToCome-(outlog[counter]-outlog[subnode.search]))
                    subnode.setCostToCome(max(subnode.costToCome,abs(subnode.x - goal.x) + abs(subnode.y - goal.y)))
                else:
                    subnode.setCostToCome(goal.x, goal.y)
                subnode.costToGo = math.inf
                subnode.search = counter
            if subnode.costToGo > (node.costToGo + action_cost):  #should be 1 for cost of moving to node, right?
                #sets subnode g value appropriately and establishes tree
                subnode.costToGo = node.costToGo + subnode.action_cost
                subnode.parent = node
                #update subnode values if the node was in the openlist
                ind = openlist.check(subnode)
                if ind != -1:
                    openlist.delete(ind)
                openlist.insert(subnode)
        actions_possible = []

def main():
    if DEBUGFLAG:
        #print("blah")
        import pdb;pdb.set_trace()
    else:
        #print("blah")
        sys.stdout = open('outputA.txt','w')
        #sys.stdout = open("output.txt",'w')
    start_time = time()
    expanded = 0
    counter = 1  #set iteration counter
    text = sys.argv[1]
    grid = open(text)
    #grid = open(sys.argv[1])
    #grid = open("C:\\Users\\epywa\\OneDrive\\Documents\\vscode\\AIProjects-master\\arrs\\randGrid\\00.txt")
    print(text)

    lstart = lgoal = start = goal = None
    while (lstart is None) or (lgoal is None) or lstart.blocked or lgoal.blocked:
    #goal = (69,25)#(random.randint(0,100),random.randint(0,100)) # tuple(column, row)
    #start = (59,50)#(random.randint(0,100),random.randint(0,100)) # tuple(column, row)
    #if False:
        start = (int(sys.argv[2]),int(sys.argv[3]))#(random.randint(0,100),random.randint(0,100)) # tuple(column, row)
        goal = (int(sys.argv[4]),int(sys.argv[5]))#(random.randint(0,100),random.randint(0,100)) # tuple(column, row)
        lstart = rgrid[start[0]][start[1]]
        lgoal = rgrid[goal[0]][goal[1]]
    #using random gen for the moment
    #initialize start and goal nodes
    rgrid = [[None for x in range(101)]for y in range(101)]
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            rgrid[i][s] = GridNode.node(i, s, math.inf, None, 0, line[s*2:s*2+2].rstrip() == "1")
            #(x, y, costToGo, parent, search, blocked)
    lstart = rgrid[start[0]][start[1]]
    lgoal = rgrid[goal[0]][goal[1]]
    print("start: (", start[0], ',', start[1],")")
    print("goal: (", goal[0], ',', goal[1],")")
    lstart.setCostToCome(goal[0], goal[1])
    lstart.costToGo = 0
    openlist = BreakLargeHeap.BLHeap()
    #outlog = [0,0]
    sgoal = 0
    #diff = 0
    while lstart != lgoal:
        lgoal.costToGo = math.inf
        #increment counter to keep track of nodes over iterations
        #initialize lists
        openlist.wipe()
        closedlist = [] #make array for now. #TODO make closed list consistent over code
        openlist.insert(lstart)
        #run A*
        ComputePath(rgrid, lgoal, openlist, closedlist, counter,sgoal)
        expanded += len(closedlist)
        if openlist.size == 0:
            print("Cannot reach target")
            return
        path = []
        #TODO move along path and implement action-cost adjustments
        #need to have ability to track changes over the path and iterate until action changes
        node = lgoal
        while node != lstart:
            path.append(node)
            node = node.parent #why
            #if node is lstart:
                #break
        path.append(lstart)
        nstart = None
        flagnode = None
        #diff += sgoal-len(path) #add difference between path lengths each run, keeping a running tally of overall difference
        #outlog.append(diff)
        sgoal = len(path)
        for i in range(sgoal,0,-1):
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
        counter += 1
    print("target reached")
    print("num-expanded:" + str(expanded))
    print("counter:" + str(counter))
    print("path_length:" + str(len(path)))
    print("start: (", start[0], ',', start[1],")")
    print("goal: (", goal[0], ',', goal[1],")")
    print("execution_time:",str(time()-start_time))

    return



if __name__ == "__main__":
    main()
