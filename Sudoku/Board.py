__author__ = 'NereWARin'
from collections import Counter
import copy
import math

class SudokuBoard():
    """
    Sudoku board state representation
    """
    def __init__(self, definedNubmers, undefinedSymbol = "x"):
        """
        self.board constructor
        :param definedNubmers: dict of predefined  {location : number} pairs
        :param undefinedSymbol: symbol for empty cells
        :return:
        """
        self.dimension = 9
        self.quadDim = math.sqrt(self.dimension)
        self.empty = undefinedSymbol
        self.board = []
        for row in range(self.dimension):
            self.rows = []
            for col in range(self.dimension):
                self.rows.append(self.empty)
            self.board.append(self.rows)
        for cell, value in definedNubmers.iteritems():
            self.board[cell[0]][cell[1]] = value
        # make backup copy
        self.initialBoard = copy.deepcopy(self.board)

    def __str__(self):
        str_board = "board state:"
        for row in self.board:
            str_board += "\n" + str(row)
        return str_board
        # return str(self.board)

    def getBoardDim(self):
        """
        :return: dimension of the board, i.e. the number of cells in a row, column or quadrant
        """
        return self.dimension

    def getQuadDim(self):
        """
        :return: dimension of quadrant side (3 by default for 3x3 quadrant of 9x9 board),
        i.e. the number of cells in a row, column of a single quadrant
        """
        return self.quadDim

    def getUndefinedSymbol(self):
        return self.empty

    def getQuadrant(self, cell):
        """
        return quadrant 3x3 number from cell index (x,y)
        :param cell: tuple (row, column)
        :return: quadrant 3x3 number
        """
        x = cell[0] // 3
        y = cell[1] // 3
        return int(x  * self.getQuadDim() + y)

    def getValue(self, cell):
        """
        :param cell: tuple (row, column)
        :return: value in this cell
        """
        return self.board[cell[0]][cell[1]]

    def setValue(self, cell, value):
        """
        :param cell: tuple (row, column)
        :return: value in this cell
        """
        self.board[cell[0]][cell[1]] = value

    def isEmpty(self, cell):
        """

        :param cell: tuple (row, column)
        :return: True if its empty, False otherwise
        """
        return self.board[cell[0]][cell[1]] == self.getUndefinedSymbol()

    def reset(self):
        """
        reset board to initial state
        """
        self.board = copy.deepcopy(self.initialBoard)

    def checkRow(self, row):
        """
        check conflicts in a given row
        :param row: row to check for duplicate numbers
        :return: dictionary vs duplicated numbers as keys and locations of duplicated numbers
        in grid as values. return empty dict if checking was passed
        """
        counter = Counter(self.board[row])
        counter[self.getUndefinedSymbol()] = 0 # we do not check number of undefined cells
        duplicated = {}
        for k, v in  counter.iteritems():
            if v > 1:
                conflicted_cells = set()
                for col in range(self.getBoardDim()):
                    if self.board[row][col] == k:
                        conflicted_cells.add((row,col))
                duplicated[k] = conflicted_cells
        return duplicated

    def checkColumn(self, col):
        """
        check conflicts in a given column
        :param col: column to check for duplicate numbers
        :return: dictionary vs duplicated numbers as keys and locations of duplicated numbers
        in grid as values. return empty dict if checking was passed
        """
        column = [self.board[row][col] for row in range(self.getBoardDim())]
        counter = Counter(column)
        counter[self.getUndefinedSymbol()] = 0 # we do not check number of undefined cells
        duplicated = {}
        for k, v in  counter.iteritems():
            if v > 1:
                conflicted_cells = set()
                for row in range(self.getBoardDim()):
                    # if self.board[row][col] == k:
                    if column[row] == k:
                        conflicted_cells.add((row,col))
                duplicated[k] = conflicted_cells
        return duplicated

    def checkQuadrant(self, index):
        """
        check conflicts in a given quadrant
        :param index: quadrant index (0..8) to check for duplicate numbers
        :return: dictionary vs duplicated numbers as keys and locations of duplicated numbers
        in grid as values. return empty dict if checking was passed
        """
        quadrant = {}
        duplicated = {}
        quadDim = self.getBoardDim()//3 # cells in a single row or column of quadrant (= 3)
        for qRow in range(quadDim):
            for qCol in range(quadDim):
                # qRow -- row relative to 3x3 quadrant
                # bRow -- row relative to 9x9 board
                bRow = qRow + (index % 3) * quadDim
                bCol = qCol + (index // quadDim) * quadDim
                cell = (bRow, bCol)
                value = self.getValue(cell)
                if quadrant.has_key(value) and value != self.getUndefinedSymbol() :
                    # conflict!
                    conflicted_cells = quadrant[value]
                    conflicted_cells.append(cell)
                    duplicated[value] = conflicted_cells
                else:
                    quadrant[value] = [cell]
        # print "quadrant:\n", quadrant
        return duplicated

## TEST SECTION
def SudokuBoardTest():
    definedNubmers = {(0,0):8,
                      (1,2):3, (1,3):6,
                      (2,1):7,(2,4):9, (2,6):2,
                      (3,1):5, (3,5):7,
                      (4,4):4, (4,5):5, (4,6):7,
                      (5,3):1, (5,7):3,
                      (6,2):1, (6,7):8, (6,8):6,
                      (7,2):8, (7,3):5, (7,7):1,
                      (8,1):9, (8,6):4      }
    TestBoard    =    SudokuBoard(definedNubmers)
    print TestBoard

    # test checkRow
    # check initial board
    assert TestBoard.checkRow(8) == {}, "checkRow failed for good testboard"
    # make conflict
    TestBoard.setValue((8,8), 4)
    assert TestBoard.checkRow(8) == {4: set([(8, 6), (8, 8)])}, "checkRow passed for conflicted testboard"
    # backup to initial board state
    # TestBoard.setValue((8,8), TestBoard.getUndefinedSymbol())
    TestBoard.reset()
    print "test checkRow passed"

    # test checkColumn
    assert TestBoard.checkColumn(1) == {}, "checkColumn failed for good testboard"
    TestBoard.setValue((1,1), 7)
    assert TestBoard.checkColumn(1) == {7: set([(1, 1), (2, 1)])}, "checkColumn passed for conflicted testboard"
    TestBoard.reset()
    print "test checkColumn passed"

    # # getQuadrant test
    # for row in range(TestBoard.getBoardDim()):
    #     for col in range(TestBoard.getBoardDim()):
    #         print (row, col), TestBoard.getQuadrant((row, col))

    # test checkQuadrant
    goodcheckQuadrant = TestBoard.checkQuadrant(0)
    # print "good checkQuadrant", goodcheckQuadrant
    assert goodcheckQuadrant == {}, "checkQuadrant failed for good testboard"
    TestBoard.setValue((1,1), 7)
    badcheckQuadrant = TestBoard.checkQuadrant(0)
    # print "bad checkQuadrant", badcheckQuadrant
    assert badcheckQuadrant == {7: [(1, 1), (2, 1)]}, "checkQuadrant failed for bad testboard"
    print "test checkQuadrant passed"



## run test
# SudokuBoardTest()