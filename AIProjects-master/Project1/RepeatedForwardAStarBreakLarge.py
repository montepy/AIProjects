import BreakLargeHeap


grid = open("..\\arrs\\randGrid\\00.txt")
rgrid = [][]
for i in list(range(101)):  #converts text grid to more easily used array form
    line = grid.readline()
    for s in list(range(101)):
        rgrid[i][s] = (line[s:s+2].rstrip(), False) #(blocked, visited)

openlist = []
closedlist = []

heap = []
def ComputePath(self,rgrid):
    loggrid = [101][101]
    


class node:
    def __init__(self, x, y, costToGo, parent):
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
