#rat in a maze
#given a maze and we have to find the correct position of to reach the last position
maze = [ [1, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 1, 0],
          [1, 1, 1, 1] ]
#rat can only move in downward and forward
n=4
#solution arr for storing the direction
solution = [[0 for j in range(n)] for i in range(n)]
def solve(maze,solution,x,y):
  if x== n-1 and y == n-1:
    solution[x][y]=1
    printit(solution,n)
    return True
  if safe(maze,x,y):
    solution[x][y] = 1
    solve(maze,solution,x+1,y)
    solve(maze,solution,x,y+1)
    #backtrack
    solution[x][y]=0
    return ""

def safe(maze,x,y):
  if x>=0 and x<n and y>=0 and y<n and maze[x][y] ==1:
    return True
  return False
def printit(solution,n):
  for i in range(n):
    for j in range(n):
      print(solution[i][j],end="")
    print()
print(solve(maze,solution,0,0))
