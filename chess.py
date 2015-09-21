"""
    Author: David Thong Nguyen
    Date Created: Dec 7th, 2013

Date Modified: Dec 7th, 2013
    - finished printBoard()
    - created classes for each Slot and the Board

    
NEXT OBJECTIVE:
    - 
"""

from chessPieces import *

class Slot():
    __slots__ = ("chesspiece","symbol",\
                 "xPos","yPos","isEmpty")
                 
class Board():
    __slots__ = ("DIM","slots","column_letter","row_number")

def mkSlot():
    slot = Slot()
    slot.chesspiece = None
    slot.symbol = " "
    slot.xPos = ""
    slot.yPos = ""
    slot.isEmpty = True
    return slot

def mkBoard():
    board = Board()
    board.DIM = 8
    board.slots = [[mkSlot() for row in range(board.DIM)]\
                   for column in range(board.DIM)]
    board.column_letter = ["a","b","c","d","e","f","g","h"]
    board.row_number = [str(i) for i in range(1,9)]
    board.row_number.reverse()
    return board


def positioning(x,y):
    if x == "a":
        x = 0
    elif x == "b":
        x = 1
    elif x == "c":
        x = 2
    elif x == "d":
        x = 3
    elif x == "e":
        x = 4
    elif x == "f":
        x = 5
    elif x == "g":
        x = 6
    elif x == "h":
        x = 7
    if y == "8":
        y = 0
    elif y == "7":
        y = 1
    elif y == "6":
        y = 2
    elif y == "5":
        y = 3
    elif y == "4":
        y = 4
    elif y == "3":
        y = 5
    elif y == "2":
        y = 6
    elif y == "1":
        y = 7
    return x,y
    

def initBoard(board):
    # assigning position
    """
    for row in range(board.DIM):
        for column in range(board.DIM):
            board.slots[row][column].yPos = board.row_number[row]
            board.slots[row][column].xPos = board.column_letter[column]
    """
    x,y = positioning("a","8")
    board.slots[x][y].symbol = "♜"
    


def movement():
    userInput = str(input("Enter x and y position: "))
    x = userInput[0]
    y = userInput[1]
    x,y = positioning(x,y)
    

def printBoard(board):
    result = "         "
    # for top row
    for i in board.column_letter:
        result += str(i) + "     "
    result += "\n       " + "=====" * board.DIM + "======="

    # for board rows\
    for row in range(board.DIM):
        result += "\n   "
        result += str(board.row_number[row]) + " ||  "
        for column in range(board.DIM):
            result += str(board.slots[row][column].symbol)
            if column != board.DIM-1:
                result += "  |  "
        result += "  || " + board.row_number[row] + "\n     "
        if row < 7:
            result += "|" + "|-----"* board.DIM + "||"
        else:
            result += "  " + "=====" * board.DIM + "======="

    # for bottom row
    result += "\n         "
    for i in board.column_letter:
        result += str(i) + "     "

    print(result)


def test(board):
    initBoard(board)
    printBoard(board)
    
    
def main():
    brd = mkBoard()
    printBoard(brd)
    input("Press ENTER to quit")
    

main()
