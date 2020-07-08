
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

    def removeMin(self):
        if self.size == 0:
            return None
        out = self.array[0]
        i = 0
        while i < len(self.array) and len(self.array) > 1:
            if self.array[int(i*2+1)].fvalue() < self.array[int(i*2+2)].fvalue():
                self.array[i] = self.array[int(i*2+1)]
                i = int(i*2+1)
            elif self.array[int(i*2+1)].fvalue() == self.array[int(i*2+2)].fvalue():
                if self.array[int(i*2+1)].costToGo > self.array[int(i*2+2)].costToGo:
                    self.array[i] = self.array[int(i*2+1)]
                    i = int(i*2+1)
                elif self.array[int(i*2+1)].costToGo < self.array[int(i*2+2)].costToGo:
                    self.array[i] = self.array[int(i*2+2)]
                    i = int(i*2+2)
            else:
                self.array[i] = self.array[int(i*2+2)]
                i = int(i*2+2)
        self.array.pop()
        self.size -= 1
        return out
    
    def insert(self, node):
        self.array.append(node)
        i = len(self.array)-1
        while node.fvalue() < self.array[int((i-1)/2)].fvalue() and i > 0:
            self.array[i] = self.array[int((i-1)/2)]
            i = int((i-1)/2)
            self.array[i] = node
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





