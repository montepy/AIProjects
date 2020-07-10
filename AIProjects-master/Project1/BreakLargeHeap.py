class BLHeap:

    def __init__(self):
        #TODO deal with heap memory allocation
        self.size = 0
        self.array = []

    def wipe(self):
        self.array = []
        self.size = 0

    def getMin(self):
        return self.array[0]

    def getPC(self, i, out):
        parent = self.array[i]
        childl = childr = out
        if len(self.array)>i*2+1:
                childl = self.array[i*2+1]
        if len(self.array)>i*2+2:
                childr = self.array[i*2+2]
        return parent, childl, childr


    def removeMin(self):
        if self.size == 0:
            return None
        out = self.array[0]
        self.array[0],self.array[self.size-1] = self.array[self.size-1], self.array[0]#swap first and last elements
        self.array.pop()
        self.size -= 1
        i = 0
        parent, childl, childr = BLHeap.getPC(self,i,out)

        #NOTE need to add code to manage when both children are equal and to address costToGo 
        while (parent.fvalue() > childl.fvalue or parent.fvalue() > childr.fvalue()) and len(self.array) > 1:
            if childl.fvalue() < childr.fvalue():
                self.array[i],self.array[i*2+1] = self.array[int(i*2+1),self.array[i]]
                i = int(i*2+1)
            elif childl.fvalue > childr.fvalue():
                self.array[i],self.array[int(i*2+2)]= self.array[int(i*2+2)],self.array[i]
                i = int(i*2+2)
            else:
                self.array[i],self.array[i*2+1] = self.array[int(i*2+1),self.array[i]]
                i = int(i*2+1)

            parent = self.array[i]
            if len(self.array)>i*2+1:
                childl = self.array[i*2+1]
            if len(self.array)>i*2+2:
                childr = self.array[i*2+2]

        while parent.fvalue() == childl.fvalue() or parent.fvalue() == childr.fvalue(): 
            if parent.fvalue() == childl.fvalue():
                if parent.costToGo > childl.costToGo:
                    break
                else:
                    self.array[i],self.array[i*2+1] = self.array[int(i*2+1),self.array[i]]
                    i = int(i*2+1)
            else:
                if parent.costToGo > childr.costToGo:
                    break
                else:
                    self.array[i],self.array[int(i*2+2)]= self.array[int(i*2+2)],self.array[i]
                    i = int(i*2+2)

            parent = self.array[i]
            if len(self.array)>i*2+1:
                childl = self.array[i*2+1]
            if len(self.array)>i*2+2:
                childr = self.array[i*2+2]


        #self.array.pop()
        #self.size -= 1
        return out
    
    def insert(self, node):
        self.array.append(node)
        i = len(self.array)-1
        while node.fvalue() < self.array[int((i-1)/2)].fvalue() and i > 0:
            self.array[i] = self.array[int((i-1)/2)]
            i = int((i-1)/2)
            self.array[i] = node
        #NOTE the if statement below might need to be changed to a while loop 
            #because multiple nodes may have the same fvalue
        if node.fvalue() == self.array[int((i-1)/2)].fvalue() and i > 0:
            if node.costToGo > self.array[int((i-1)/2)].costToGo:
                self.array[i] = self.array[int((i-1)/2)]
                i = int((i-1)/2)
                self.array[i] = node
        self.size += 1
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
        self.removeMin()
        self.size -= 1
        return True

    def check(self, node):
        #i'm lazy, so simple linear search for now
        counter = 0
        for i in self.array:
            if i.x == node.x and i.y == node.y:
                return counter
            counter += 1
        return -1





