
grid = open("..\\arrs\\randGrid\\00.txt")
rgrid = [][]
for i in list(range(101)):  #converts text grid to more easily used array form
    line = grid.readline()
    for s in list(range(101)):
        rgrid[i][s] = (line[s:s+2].rstrip(), False) #(blocked, visited)

heap = []
def ComputePath(self,rgrid):
    loggrid = [101][101]
