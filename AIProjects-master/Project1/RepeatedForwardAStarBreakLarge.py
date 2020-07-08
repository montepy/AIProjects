import BreakLargeHeap


def ComputePath(rgrid, goal, openlist, closedlist):
    #loggrid = [101][101]
    #TODO finish implementing A* later.
    while goal.costToGo > openlist.getMin().fvalue():  #while smallest f-value less than goal g value
        #basically, while goal has not been reached, or fvalue() is greater than infinity, indicating a blocked path
        #take smallest node and expand
        node = openlist.removeMin()
        actions_possible = node.expand(openlist, closedlist, rgrid)
        closedlist.add(node)
        for subnode in out:
            action_cost = 1
            if subnode.blocked:
                action_cost = 100000000
            subnode.goalPosition(goal.x,goal.y)
            if subnode.search < counter:
                #if search value(last time encountered) is less than counter, set search to counter and 
                #set g value to infinity to ensure next if statement triggers
                subnode.costToGo = int('inf')
                subnode.search = counter
            if subnode.costToGo > (node.CosttoGo + action_cost): #should be 1 for cost of moving to node, right?
                #sets subnode g value appropriately and establishes tree
                subnode.costToGo = node.CosttoGo + action_cost
                subnode.parent = node
                #update subnode values if the node was in the openlist
                ind = openlist.check(subnode)
                if ind != -1:
                    openlist.delete(ind)
                openlist.insert(subnode)








def main():
    counter = 0  #set iteration counter
    grid = open("..\\arrs\\randGrid\\00.txt")
    rgrid = [101][101]
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            rgrid[i][s] = node(i, s, int('inf'), None, 0, line[s:s+2].rstrip() == "1")
            #(x, y, costToGo, parent, search, blocked)
    
    goal =  # tuple(column,row)
    start =  # tuple(column, row)
    #don't know how I'm supposed to generate these. Tabling for now
    search = 0
    #initialize start and goal nodes
    lstart = rgrid[start[0]][start[1]]
    lgoal = rgrid[goal[0]][goal[1]]
    lgoal.costToGo = int('inf') 
    lstart.goalPosition(goal[0], goal[1])
    while lstart != lgoal:
        #increment counter to keep track of nodes over iterations
        counter = counter+1
        #initialize lists
        openlist = BlHeap()
        closedlist = [] #make array for now. #TODO make closed list consistent over code
        openlist.insert(lstart)
        #run A*
        ComputePath(rgrid, lstart, lgoal, openlist, closedlist)
        if openlist.size == 0:
            print("Cannot reach target")
            return
        path = []
        #TODO move along path and implement action-cost adjustments
        #need to have ability to track changes over the path and iterate until action changes
        node = lgoal
        while node.parent != None:
            path.append(node)
            node = node.parent
        check = path[len(path)-1]
        flagnode = None
        for i in list(len(path)):
            #TODO implement later. 
            if check == goal:
                break
            if path[len(path)-1-i].costToGo- check.costToGo > 1:
                flagnode = path[len(path)-1-i]
                break
            check = path[len(path)-1-i]
        lstart = check
        if flagnode:
            flagnode.costToGo = int('inf')
    print("target reached")
    return

            
            
        


class node:
    def __init__(self, x, y, costToGo, parent, search, blocked):
        #self.name = name
        self.x = x
        self.y = y
        self.costToGo = costToGo
        #self.costToCome = costToCome
        self.parent = parent
        self.findCostToCome()
        self.blocked = blocked
        self.search = search
        
    def setSearch(self, nval):
        self.search = nval
        return

    def findCostToCome(self):
        self.costToCome = abs(self.x - goal_x) + abs(self.y - goal_y)
        return

    def setParent(self, parent):
        self.parent = parent
        return

    def fvalue(self):
        return findCostToCome()+self.costToGo
        
    def goalPosition(self, x, y):
        goal_x = x
        goal_y = y
        return

    def __eq__(self,other):
        if not isinstance(other, node):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.search == other.search

    def expand(self, openlist, closedlist, rgrid):
        #for i in closedlist:    #note: will need to put all the blocked cells into the closed list for this to work
            #if (self.x == i.x and self.y == i.y):
                #openlist.remove(self)
                #closedlist.append(self) #doesn't really need to be in the closed list, only takes up extra space
                #return
        #I feel like the above isn't really needed, provided we do everything correctly in the rest of the code

        #expand and insert neighbors to openlist
        #I think I got all of the below wrong. commenting out for now.
        #if self.y+1 < 101 and not rgrid[self.x][self.y+1].blocked:
        #    rgrid[self.x][self.y+1].costToGo = self.costToGo+1
        #    rgrid[self.x][self.y+1].setParent(self)
        #    openlist.insert(rgrid[self.x][self.y+1])
        #if self.y-1 >= 0 and not rgrid[self.x][self.y-1].blocked:
        #    rgrid[self.x][self.y-1].setParent(self)
        #    rgrid[self.x][self.y-1].costToGo = self.costToGo+1
        #    openlist.insert(rgrid[self.x][self.y-1])
        #if self.x+1 < 101 and not rgrid[self.x+1][self.y].blocked:
        #    rgrid[self.x+1][self.y].costToGo.setParent(self)
        #    rgrid[self.x+1][self.y].costToGo = self.costToGo+1
        #    openlist.insert(rgrid[self.x+1][self.y])
        #if self.x-1 >= 0 and not rgrid[self.x-1][self.y].blocked:
        #    rgrid[self.x-1][self.y].setParent(self)
        #    rgrid[self.x-1][self.y].costToGo = self.costToGo+1
        #    openlist.insert(rgrid[self.x-1][self.y])
        #n = node(self.y-1, self.x, self.costToGo+1, self)
        #openlist.append(n)
        #s = node(self.y+1, self.x, self.costToGo+1, self)
        #openlist.append(s)
        #e = node(self.y, self.x+1, self.costToGo+1, self)
        #openlist.append(e)
        #w = node(self.y, self.x-1, self.costToGo+1, self)
        #openlist.append(w)
        
        #openlist.remove(self)
        #pain in the butt to remove manually, what with heaps being what they are. 
        #Considering we're always popping off the top of the heap, we shouldn't need the above
        #closedlist.insert(self)
        out = []
        out.append(rgrid[self.x+1][self.y])
        out.append(rgrid[self.x-1][self.y])
        out.append(rgrid[self.x][self.y+1])
        out.append(rgrid[self.x][self.y-1])
        return out


if __name__ == "__main__":
    main()