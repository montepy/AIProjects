
class node:
    def __init__(self, x, y, costToGo, parent, search, blocked):
        #self.name = name
        self.x = x
        self.y = y
        self.costToGo = costToGo
        #self.costToCome = costToCome
        self.parent = parent
        #self.findCostToCome()
        self.blocked = blocked
        self.search = search
        self.costToCome = 0
        
    def setSearch(self, nval):
        self.search = nval
        return

    def setCostToCome(self, goal_x, goal_y):
        self.costToCome = abs(self.x - goal_x) + abs(self.y - goal_y)
        return

    def setParent(self, parent):
        self.parent = parent
        return

    def fvalue(self):
        return self.costToCome+self.costToGo
        
    #def goalPosition(self, x, y):
    #    self.goal_x = x
    #    self.goal_y = y
    #    return

    def __eq__(self, other):
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
        if self.x+1 <101:
            out.append(rgrid[self.x+1][self.y])
        if self.x > 0:
            out.append(rgrid[self.x-1][self.y])
        if self.y < 101:
            out.append(rgrid[self.x][self.y+1])
        if self.y > 0:
            out.append(rgrid[self.x][self.y-1])
        return out
