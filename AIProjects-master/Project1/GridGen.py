import random
import collections
#start here


random.seed()
rows, cols = 101, 101
#generate grid of 101x101
grid = [[(0, False)]*cols]*rows
#first is blocked, second is visited
entry = (random.randint(0, 100), random.randint(0, 100))  #pick random block
stack = collections.deque()
stack.append(entry)
while stack:
    check = stack.pop()
    blocked = 0
    toblock = random.random()
    if toblock < 0.3:  #if 30% chance of blocked met, set blocked
        blocked = 1
    grid[check[0]][check[1]] = (blocked, True)  #set visited
    if check[1]+1 <= 100 and grid[check[0]][check[1]+1][1] is not True:
        stack.append((check[0], check[1]+1))
    if check[1]-1 >= 0 and grid[check[0]][check[1]-1][1] is not True:
        stack.append((check[0], check[1]-1))
    if check[0]+1 <= 100 and grid[check[0]+1][check[1]][1] is not True:
        stack.append((check[0]+1, check[1]))
    if check[0]-1 >= 0 and grid[check[0]-1][check[1]][1] is not True:
        stack.append((check[0]-1, check[1]))
    #add all possible adjacent blocks to stack for exploration
    #pop unchecked block off of stack

print(grid)