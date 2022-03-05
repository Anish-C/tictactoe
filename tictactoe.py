board= [
    "-","-","-",
    "-","-","-",
    "-","-","-"]
winner= None
gamerunning=True
def printboard (board):
    print (board [0]+"  |  "+board [1]+"  |  "+board [2])
    print (board [3]+"  |  "+board [4]+"  |  "+board [5])
    print (board [6]+"  |  "+board [7]+"  |  "+board [8])



def player (user_input):
    inp= int (input("Enter a position 1-9 "))
    if inp>0 and inp <10 and board [inp-1]=="-":
        board [inp-1]=currentplayer
    else:
        print (" play the game right")

#finds the winner
def checkrow (board):
    global winner
    if board [0]==board [1]==board [2] and board[1]!= '-':
        winner=board [1]
        return True
    elif board [3]==board [4]==board [5] and board[4]!= '-':
        winner=board [1]
        return True
    elif board [6]==board [7]==board [8] and board[7]!= '-':
        winner=board [1]
        return True
def checkdiag (board):
    if board [0]==board [4]==board [8] and board[4]!= '-':
        winner=board [4]
        return True
    elif board [2]==board [4]==board [6] and board[4]!= '-':
        winner=board [4]
        return True
def checkcolumn (board):
    global winner
    if board [0]==board [3]==board [6] and board[0]!= '-':
        winner=board [0]
        return True
    elif board [1]==board [4]==board [7] and board[4]!= '-':
        winner=board [1]
        return True
    elif board [2]==board [5]==board [8] and board[8]!= '-':
        winner=board [2]
        return True
def checkwin(board):
    global gamerunning
    if checkdiag(board) or checkcolumn (board) or checkrow(board):
        print(f"the winner is {winner}")
        gamerunning=False

def checktie (board):
    global gamerunning
    global winner
    if "-" not in board and winner==None:
        printboard(board)
        print ("tie")
        winner='neither of you'
        gamerunning= False

currentplayer= "X"
#switches player
def switcher (board):
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    elif currentplayer=="O":
        currentplayer="X"

while gamerunning:
      printboard(board)
      player (board)
      switcher(board)
      checkwin(board)
      checktie(board)
      
