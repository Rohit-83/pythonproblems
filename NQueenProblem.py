#Number of queens
print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for i in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking left diagonals
    r=i-1
    c=j-1
    while r>=0 and c>=0:
      if board[i][j] == 1:
        return True
      r=r-1
      c=c-1
    #checking right diagonal
    r1=i-1
    c1=j+1
    while r1>=0 and c1<N:
      if board[r1][c1] == 1:
        return True
      r1=r1-1
      c1=c1+1
    
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queen(N)
for i in board:
    print (i)
