
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
    

    
#need to create closedlists and open list. 
#open list is a priority que that organizes lists by nodes which represents the 

class node:
    def __init__(self, name, x, y, costToGo, costToCome,parent):
        self.name = name
        self.x = x
        self.y = y
        self.costToGo = costToGo
        self.costToCome = costToCome
        self.parent = parent

    def expand()
        for i in closedlist:
            if (this.x == i.x and this.y == i.y):
                openlist.remove(this)
                #closedlist.append(this) #doesn't really need to be in the closed list, only takes up space
                return
            
        #need code to find the cost to come
        n = node(this.name + "_north", this.y-1, this.x, this.costToGo+1, *COSTTOCOMEVAR, this)
        openlist.append(n)
        s = node(this.name + "_south", this.y+1, this.x, this.costToGo+1, *COSTTOCOMEVAR, this)
        openlist.append(n)
        e = node(this.name + "_east", this.y, this.x+1, this.costToGo+1, *COSTTOCOMEVAR, this)
        openlist.append(n)
        w = node(this.name + "_west", this.y, this.x-1, this.costToGo+1, *COSTTOCOMEVAR, this)
        openlist.append(n)
        
        openlist.remove(this)
        closedlist.append(this)
        return
