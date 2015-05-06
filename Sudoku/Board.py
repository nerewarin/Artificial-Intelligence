__author__ = 'NereWARin'
from collections import Counter
import copy
import math
import TestGlobals

class SudokuBoard():
    """
    Sudoku board state representation
    """
    def __init__(self, definedNubmers, undefinedSymbol = "x", numbers = range(1, 10)):
        """
        self.board constructor
        :param definedNubmers: dict of predefined  {location : number} pairs
        :param undefinedSymbol: symbol used for marking empty cells
        :param numbers: list -- what numbers can be placed to cell
        :return:
        """
        self.numbers = numbers
        self.dimension = len(numbers)
        self.quadDim = int(math.sqrt(self.dimension))
        self.empty = undefinedSymbol
        self.board = []
        for row in range(self.dimension):
            self.rows = []
            for col in range(self.dimension):
                self.rows.append(self.empty)
            self.board.append(self.rows)
        for cell, value in definedNubmers.iteritems():
            self.board[cell[0]][cell[1]] = value
        # compute all variants for every cell
        self.ValuesVariants = self.allValuesVariants()
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

    def copy(self):
        return copy.deepcopy(self)

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
        quadDim = self.getQuadDim() # cells in a single row or column of quadrant (= 3)
        # start_cell = ( (index % 3) * quadDim, (index // quadDim )* quadDim)
        start_cell = ( (index // quadDim) * quadDim, (index % quadDim )* quadDim)
        for qRow in range(quadDim):
            for qCol in range(quadDim):
                # qRow -- row relative to 3x3 quadrant
                # bRow -- row relative to 9x9 board
                bRow = qRow + (index // quadDim) * quadDim
                bCol = qCol + (index % quadDim) * quadDim
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

    def checkAll(self, cell = "all"):
        """
        check row, col and quadrant for 1 cell or for every cell
        :param cell:
        :return: tuple of results (checkRow, checkColumn, checkQuadrant), where each result has form
        {conflicted row/col/quad : {number : set(cell1, cell2..) } }
        """
        rowConflicts = {}
        colConflicts = {}
        quadConflicts = {}

        if cell == "all":
            rRange = range(self.getBoardDim())
            cRange = range(self.getBoardDim())
            qRange = range(self.getBoardDim())
        else:
            # only one cell, so 1 row, 1 col and 1 quadrant
            rRange = range(cell[0], cell[0] + 1)
            cRange = range(cell[1], cell[1] + 1)
            quad = self.getQuadrant(cell)
            qRange = range(quad, quad + 1)

        # if cell == "all":
        for row in rRange:
            rCheck = self.checkRow(row)
            if rCheck:
                # print "row conflict", rCheck
                rowConflicts[row] = rCheck
        # for col in range(self.getBoardDim()):
        for col in cRange:
            cCheck = self.checkColumn(col)
            if cCheck:
                # print "column conflict", cCheck
                colConflicts[col] = cCheck
        for quad in qRange:
            # print "check quad", quad
            qCheck = self.checkQuadrant(quad)
            if qCheck:
                # print "quadrant conflict", qCheck
                quadConflicts[quad] = qCheck
        return rowConflicts, colConflicts, quadConflicts

    def isFull(self):
        """

        :param board:
        :return:
        """
        # print self.getUndefinedSymbol(), self.board
        for row in self.board:
            if self.getUndefinedSymbol()  in row:
                # print "notFull"
                return False
        return True

    # def isGoal(self):
    #     """
    #
    #     :return: True if solution complete
    #     """

    def getNumbers(self):
        return self.numbers

    def valuesVariants(self, cell):
        """
        returns values that we can place in a given cell not violating constraints
        :param board: Sudoku board state
        :param cell:
        :return:
        """
        if not self.isEmpty(cell):
            return [self.getValue(cell)]
        variants = self.getNumbers()
        result = []
        for value in variants:
            brd = self.copy()
            brd.setValue(cell, value)
            # print "cell", cell, "var", value, brd.checkAll(cell)
            problems = False
            for problem in  brd.checkAll(cell):
            # if  brd.checkAll(cell) != ({}, {}, {}):
                if problem: problems = True
            if not problems:
                result.append(value)
        return result

    def allValuesVariants(self):
        """
        compute valuesVariants for every cell
        :param board:
        :return: list of lists (variants in cell 0,0 .. 0,1 ... 0,x.. x,x)
        """
        bDim = range(self.getBoardDim())
        return [self.valuesVariants((row, col)) for row in bDim for col in bDim]

    def getVariants(self, cell = "all"):
        if cell == "all":
            return self.ValuesVariants
        return self.ValuesVariants[self.cellToIndex(cell)]

    def cellToIndex(self, (row, col)):
        """
        comvert tuple (row, col) to index
        :return:
        """
        return row * self.getBoardDim()+ col

    def MRV(self, board):
        """
        Minimum Remaining Values

        :param board:  Sudoku board state
        :return: cell index corresponds to minimum number of values variant
        if there are several cells vs the same variants numbers exists, returns the last
        """

        # values in every cell -- self.allValuesVariants()
        bDim = board.getBoardDim()
        cell = (None, None)
        minValue = board.getBoardDim()
        values = self.getNumbers() # [1, 2, .. , 9]
        for ind, allValues in enumerate(self.allValuesVariants()):
            # print ind, variants, len(variants)
            lenValues = len(allValues)
            if lenValues < minValue and lenValues > 1:
                cell = (ind // bDim, ind % bDim)
                minValue = lenValues
                values = allValues
                # print cell, ind, allValues
        return cell, values



## TEST SECTION
def SudokuBoardTest():
    # definedNubmers = {(0,0):8,
    #                   (1,2):3, (1,3):6,
    #                   (2,1):7,(2,4):9, (2,6):2,
    #                   (3,1):5, (3,5):7,
    #                   (4,4):4, (4,5):5, (4,6):7,
    #                   (5,3):1, (5,7):3,
    #                   (6,2):1, (6,7):8, (6,8):6,
    #                   (7,2):8, (7,3):5, (7,7):1,
    #                   (8,1):9, (8,6):4      }
    TestBoard         = SudokuBoard(TestGlobals.definedNubmers_HB())
    TestCompleteBoard = SudokuBoard(TestGlobals.definedNubmers_COMPLETE())
    # print TestBoard

    # test checkRow
    # check initial board
    assert TestBoard.checkRow(8) == {}, "checkRow failed for good testboard"
    # make conflict
    TestBoard.setValue((8,8), 4)
    assert TestBoard.checkRow(8) == {4: set([(8, 6), (8, 8)])}, "checkRow passed for conflicted testboard"
    # backup to initial board state
    # TestBoard.setValue((8,8), TestBoard.getUndefinedSymbol())
    TestBoard.reset()
    print "passed test checkRow"

    # test checkColumn
    assert TestBoard.checkColumn(1) == {}, "checkColumn failed for good testboard"
    TestBoard.setValue((1,1), 7)
    assert TestBoard.checkColumn(1) == {7: set([(1, 1), (2, 1)])}, "checkColumn passed for conflicted testboard"
    TestBoard.reset()
    print "passed test checkColumn"

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
    TestBoard.reset()

    # TestBoard.setValue((0,3), 9)
    # print TestBoard.checkQuadrant(1)
    print "passed test checkQuadrant"

    # test checkAll
    TestBoard.reset()
    # print TestBoard.checkAll((0,1))
    assert TestBoard.checkAll((0,1)) == ({}, {}, {}), "checkall failed for good testboard in cell mode"
    assert TestBoard.checkAll() == ({}, {}, {}), "checkall failed for good testboard in all mode"
    # make conflict
    TestBoard.setValue((8,8), 4)
    assert TestBoard.checkAll() == ({8: {4: set([(8, 6), (8, 8)])}}, {}, {8: {4: [(8, 6), (8, 8)]}}), \
        "checkall passed for bad testboard in all mode"
    assert TestBoard.checkAll((8, 2)) == ({8: {4: set([(8, 6), (8, 8)])}}, {}, {}), \
        "checkall passed for bad testboard in cell mode"
    print "passed test checkAll"

    # test isFull
    TestBoard.reset()
    # print TestBoard.isFull()
    assert not TestBoard.isFull(), "goalCheck failed for uncomplited board"
    assert TestCompleteBoard.isFull(), "goalCheck failed for complited board"
    print "passed test isFull"

    # test valuesVariants
    # TestCSP = CSP()
    assert TestBoard.valuesVariants((0,3)) == [2, 3, 4, 7], "valuesVariants failed for HB (0,3)"
    assert TestBoard.valuesVariants((0,1)) == [1, 2, 4, 6], "valuesVariants failed for HB (0,1)"
    # boardDim = TestBoard.getBoardDim()
    # for row in range(boardDim):
    #     for col in range(boardDim):
    #         print (row, col), TestCSP.valuesVariants(TestBoard, (row, col))#, TestGlobals.valuesVariants_answerHB()[row*boardDim + col]
            # print str(TestCSP.valuesVariants(TestBoard, (row, col))) + ","

    #         assert TestCSP.valuesVariants(TestBoard, (row, col)) == \
    #                TestGlobals.valuesVariants_answerHB()[row * boardDim+ col], "valuesVariants failed for HB"
    print "passed test valuesVariants "

    # test allValuesVariants
    assert TestBoard.allValuesVariants() == \
                   TestGlobals.valuesVariants_answerHB(), "allvaluesVariants failed for HB"
    print "passed test allValuesVariants"

    # test getVariants
    # print TestBoard.getVariants()
    # print TestBoard.getV ariants((0,1))
    assert TestBoard.getVariants((0,1)) == [1, 2, 4, 6], "getVariants failed for HB (0,1)"

    # test MRV
    # print TestCSP.MRV(TestBoard)
    assert TestBoard.MRV(TestBoard) == ((7, 6), [3, 9]), "MVR failed for HB"
    print "passed test MVR"



## run test
if __name__ == "__main__":
    SudokuBoardTest()