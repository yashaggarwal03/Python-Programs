import numpy as np

def show_board():
 return (np.array([[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]))
def row_win(board, player):
 for x in range(len(board)):
  win = True
 for y in range(len(board)):
  if board[x, y] != player:
    win = False
    continue
  if win == True:
      return (win)
 
 return (win)

 
def diag_win(board, player):
 win = True
 y = 0
 for x in range(len(board)):
  if board[x, x] != player:
   win = False
   win = True
  if win:
   for x in range(len(board)):
    y = len(board) - 1 - x
    if board[x, y] != player:
       win = False
       return win

 

def entry(board, player):
 x, y = [int(x) for x in input("Enter two value1: ").split()]
 board[(x, y)] = player
 return (board)
# Tic-Tac-Toe game submitted by Amit Kumar Mitra

board = show_board()
print(board)
winner = 0
while winner == 0:
 counter = 1
 for player in [1, 2]:
  board = entry(board, player)
  print("Board after " + str(counter) + " move")
  print(board)
  counter += 1
  winner = evaluate(board)
  if winner != 0:
   break
print("Player " + str(winner) + "Wins")

def evaluate(board):
    winner = 0
    for player in [1, 2]:
     if (row_win(board, player) or col_win(board, player) or diag_win(board, player)):
        winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def col_win(board, player):
  for x in range(len(board)):
    win = True
    for y in range(len(board)):
        if board[y][x] != player:
         win = False
         continue
    if win == True:
        return (win)
    return (win)
