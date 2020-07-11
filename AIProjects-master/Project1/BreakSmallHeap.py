#finds smaller g values than with BGHeap
import math
class BSHeap:

    def __init__(self):
        #TODO deal with heap memory allocation
        self.size = 0
        self.maxsize = 3
        self.array = [None]*self.maxsize

    def wipe(self):
        self.size = 0
        self.maxsize = 3
        self.array = [None]*self.maxsize

    def getMin(self):
        return self.array[0]

    def getPC(self, i, out):
        parent = self.array[i]
        childl = childr = out
        if self.size>i*2+1:
            childl = self.array[i*2+1]
        if self.size>i*2+2:
            childr = self.array[i*2+2]
        return parent, childl, childr


    def removeMin(self):
        if self.size == 0:
            return None
        out = self.array[0]
        self.array[0] = None
        self.size -= 1
        if self.size == 0:
            return out
        self.array[0],self.array[self.size] = self.array[self.size], self.array[0]#swap first and last elements
        i = 0
        parent, childl, childr = BLHeap.getPC(self,i,out)

        #why is this so much more complicated than it needs to be?
        while (parent.fvalue() > childl.fvalue() or parent.fvalue() > childr.fvalue()) and self.size > 1:
            #if left child lesser. Wait, why are these size checks here when the bottom code handles it? Commenting out.
            if childl.fvalue() < childr.fvalue() and self.size > i*2+1:
                self.array[i],self.array[i*2+1] = self.array[int(i*2+1)],self.array[i]
                i = int(i*2+1)
            #if right child lesser
            elif childl.fvalue() > childr.fvalue() and self.size > i*2+2:
                self.array[i],self.array[int(i*2+2)]= self.array[int(i*2+2)],self.array[i]
                i = int(i*2+2)
            #if the two are equal
            elif childl.fvalue() == childr.fvalue() and self.size > i*2+2:
                if childl.costToGo > childr.costToGo:
                    self.array[i],self.array[i*2+1] = self.array[int(i*2+1)],self.array[i]
                    i = int(i*2+1)
                #favor right, doesn't matter
                else:
                    self.array[i],self.array[int(i*2+2)]= self.array[int(i*2+2)],self.array[i]
                    i = int(i*2+2)
            else:
                break
            #previous issue with this code is that child object stayed constant if next level 
            #not existent resulting in erroneous swaps
            parent = self.array[i]
            if self.size>i*2+1:
                childl = self.array[i*2+1]
            else:
                childl = None
            if self.size>i*2+2:
                childr = self.array[i*2+2]
            else:
                childr = None
            #only handle case where (childl and not childr) because (not childl and childr) is not a case that should ever happen
            #if working correctly
            #sometimes i wish python could just take None as a False value.
            if childr is None:
                if childl is not None:
                    #swap in and break if left child better, otherwise return because this is end of array
                    if childl.fvalue() < parent.fvalue() or (childl.fvalue() == parent.fvalue() and childl.costToGo > parent.costToGo):
                        self.array[i],self.array[i*2+1] = self.array[int(i*2+1)],self.array[i]
                        i = int(i*2+1)
                return out


        while parent.fvalue() == childl.fvalue() or parent.fvalue() == childr.fvalue(): 
            #removed break statements
            if parent.fvalue() == childl.fvalue() and self.size > i*2+1:
                #swap if the left child lesser or if the two are equal
                if parent.costToGo < childl.costToGo:
                    break
                else:
                    self.array[i],self.array[i*2+1] = self.array[int(i*2+1)],self.array[i]
                    i = int(i*2+1)
                
            elif parent.fvalue() == childr.fvalue() and self.size > i*2+2:
                #swap if the right child lesser or if the two are equal
                if parent.costToGo < childr.costToGo:
                    break
                else:
                    self.array[i],self.array[int(i*2+2)]= self.array[int(i*2+2)],self.array[i]
                    i = int(i*2+2)
            else:
                break
            #same as before. should've just made this a function, but it's here
            parent = self.array[i]
            if self.size>i*2+1:
                childl = self.array[i*2+1]
            else:
                childl = None
            if self.size>i*2+2:
                childr = self.array[i*2+2]
            else:
                childr = None
            #only handle case where (childl and not childr) because (not childl and childr) is not a case that should ever happen
            #if working correctly
            if childr is None:
                if childl is not None:
                    #the edgiest of edge cases. gonna leave the first term here just in case
                    if childl.fvalue() < parent.fvalue() or (childl.fvalue() == parent.fvalue() and childl.costToGo > parent.costToGo):
                        self.array[i],self.array[i*2+1] = self.array[int(i*2+1)],self.array[i]
                        i = int(i*2+1)
                #should break whether or not childl b
                break

        #original code
        #self.array.pop()
        #self.size -= 1
#       i = 0
#        while i*2 < len(self.array) and len(self.array) > 1:
#            if self.array[int(i*2+1)].fvalue() < self.array[int(i*2+2)].fvalue():
#                self.array[i] = self.array[int(i*2+1)]
#                i = int(i*2+1)
#            elif self.array[int(i*2+1)].fvalue() == self.array[int(i*2+2)].fvalue():
#                if self.array[int(i*2+1)].costToGo > self.array[int(i*2+2)].costToGo:
#                    self.array[i] = self.array[int(i*2+1)]
#                    i = int(i*2+1)
#                elif self.array[int(i*2+1)].costToGo < self.array[int(i*2+2)].costToGo:
#                    self.array[i] = self.array[int(i*2+2)]
#                    i = int(i*2+2)
#            else:
#                self.array[i] = self.array[int(i*2+2)]
#                i = int(i*2+2)
#        self.array.pop()
#        self.size -= 1
        return out
    
    def insert(self, node):
        
        if (self.size + 1) == self.maxsize:
            self.allocateMemory()
        self.size += 1
        self.array[self.size-1] = node
        #self.array.append(node)
        i = self.size-1  #len(self.array)-1
        while node.fvalue() < self.array[int((i-1)/2)].fvalue() and i > 0:
            self.array[i],self.array[int((i-1)/2)] = self.array[int((i-1)/2)], self.array[i]
            i = int((i-1)/2)
            #self.array[i] = node
        if node.fvalue() == self.array[int((i-1)/2)].fvalue() and i > 0:
            if node.costToGo > self.array[int((i-1)/2)].costToGo:
                
                self.array[i],self.array[int((i-1)/2)] = self.array[int((i-1)/2)], self.array[i]
                i = int((i-1)/2)
                #self.array[i] = node
        return

    def delete(self, index):
        i = index
        if i >= self.size:
            return False
        self.array[i].costToGo = -10000
        while self.array[i].fvalue() < self.array[int((i-1)/2)].fvalue() and i > 0:
            temp = self.array[i]
            self.array[i] = self.array[int((i-1)/2)]
            i = int((i-1)/2)
            self.array[i] = temp
        if self.array[i].fvalue() == self.array[int((i-1)/2)].fvalue() and i > 0:
            if self.array[i].costToGo > self.array[int((i-1)/2)].costToGo:
                temp = self.array[i]
                self.array[i] = self.array[int((i-1)/2)]
                i = int((i-1)/2)
                self.array[i] = temp
        ex = self.removeMin()
        ex.costToGo = math.inf
        #self.size -= 1
        return True

    def check(self, node):
        #i'm lazy, so simple linear search for now
        counter = 0
        for i in list(range(self.size-1)):
            if self.array[i].x == node.x and self.array[i].y == node.y:
                return counter
            counter += 1
        return -1
    
    def allocateMemory(self):
        self.maxsize = self.maxsize*2
        newarray = [None]*self.maxsize
        for i in list(range(self.size)):
            newarray[i] = self.array[i]
        self.array = newarray
        return






