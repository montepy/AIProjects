import BreakLargeHeap

def ComputePath(self,rgrid,goal,openlist,closedlist):
    loggrid = [101][101]
    #TODO implement A* in earnest


def main():
    counter = 0 #set iteration counter
    grid = open("..\\arrs\\randGrid\\00.txt")
    rgrid = [][]
    for i in list(range(101)):  #converts text grid to more easily used array form
        line = grid.readline()
        for s in list(range(101)):
            rgrid[i][s] = (line[s:s+2].rstrip(), False,0) #(blocked, visited,generated during xth search)
    
    goal = # tuple(column,row)
    start = # tuple(column, row)
    #don't know how I'm supposed to generate these
    search = 0
    while start != goal:
        #increment counter to keep track of nodes over iterations
        counter = counter+1
        
        #initialize start and goal nodes
        lstart = node(start[0],start[1],0,None,counter)
        lgoal = node(goal[0],goal[1],0,None,counter)
        lgoal.costToGo = float('inf')
        lstart.goalPosition(goal[0],goal[1])

        #initialize lists
        openlist = BlHeap()
        closedlist = BLHeap()
        openlist.insert(lstart)
        #run A* 
        ComputePath(rgrid,goal,openlist,closedlist)
        if openlist.size == 0:
            print("Cannot reach target")
            return
        path = []
        #TODO move along path and implement action-cost adjustments





    
    


class node:
    def __init__(self, x, y, costToGo, parent,search):
        #self.name = name
        self.x = x
        self.y = y
        self.costToGo = costToGo
        #self.costToCome = costToCome
        self.parent = parent
        self.findCostToCome()
        
    def findCostToCome():
        self.costToCome = abs(self.x - goal_x) + abs(self.y - goal_y)
    def fvalue():
        return findCostToCome()+self.costToGo
        
    def goalPosition(x, y):
        goal_x = x
        goal_y = y
        return

    def expand()
        for i in closedlist:    #note: will need to put all the blocked cells into the closed list for this to work
            if (self.x == i.x and self.y == i.y):
                openlist.remove(self)
                #closedlist.append(self) #doesn't really need to be in the closed list, only takes up extra space
                return
        
        n = node(self.y-1, self.x, self.costToGo+1, self)
        openlist.append(n)
        s = node(self.y+1, self.x, self.costToGo+1, self)
        openlist.append(s)
        e = node(self.y, self.x+1, self.costToGo+1, self)
        openlist.append(e)
        w = node(self.y, self.x-1, self.costToGo+1, self)
        openlist.append(w)
        
        openlist.remove(self)
        closedlist.append(self)
        return


if __name__== "__main__":
    main()