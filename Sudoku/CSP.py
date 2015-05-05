__author__ = 'NereWARin'
import Board, TestGlobals

class CSP():
    def __init__(self, numbers = range(1, 10)):
        self.numbers = numbers

    def getNumbers(self):
        return self.numbers

    def valuesVariants(self, board, cell):
        """
        returns values that we can place in a given cell not violating constraints
        :param board: Sudoku board state
        :param cell:
        :return:
        """
        if not board.isEmpty(cell):
            return [board.getValue(cell)]
        variants = self.getNumbers()
        result = []
        for value in variants:
            brd = board.copy()
            brd.setValue(cell, value)
            # print "cell", cell, "var", value, brd.checkAll(cell)
            problems = False
            for problem in  brd.checkAll(cell):
            # if  brd.checkAll(cell) != ({}, {}, {}):
                if problem: problems = True
            if not problems:
                result.append(value)
        return result

    def allValuesVariants(self, board):
        """
        compute valuesVariants for every cell
        :param board:
        :return: list of lists (variants in cell 0,0 .. 0,1 ... 0,x.. x,x)
        """
        bDim = range(board.getBoardDim())
        return [self.valuesVariants(board, (row, col)) for row in bDim for col in bDim]

    def MRV(self, board):
        """
        Minimum Remaining Values

        :param board:  Sudoku board state
        :return: cell index corresponds to minimum number of values variant
        if there are several cells vs the same variants numbers exists, returns the last
        """

        # values in every cell -- self.allValuesVariants(board)
        bDim = board.getBoardDim()
        cell = (None, None)
        minValue = board.getBoardDim()
        for ind, allValues in enumerate(self.allValuesVariants(board)):
            # print ind, variants, len(variants)
            variants = len(allValues)
            if variants < minValue and variants > 1:
                cell = (ind // bDim, ind % bDim)
                minValue = variants
                # print cell, ind
        return cell

    def BacktrackingSearch(self, board):
        if board.isGoal():
            return board
        else:
            # TODO

def CSPtest():
    # test valuesVariants
    TestBoard    =    Board.SudokuBoard(TestGlobals.definedNubmers_HB())
    TestCSP = CSP()
    assert TestCSP.valuesVariants(TestBoard, (0,3)) == [0, 2, 3, 4, 7], "valuesVariants failed for HB (0,3)"
    assert TestCSP.valuesVariants(TestBoard, (0,1)) == [0, 1, 2, 4, 6], "valuesVariants failed for HB (0,1)"
    # boardDim = TestBoard.getBoardDim()
    # for row in range(boardDim):
    #     for col in range(boardDim):
    #         print (row, col), TestCSP.valuesVariants(TestBoard, (row, col))#, TestGlobals.valuesVariants_answerHB()[row*boardDim + col]
            # print str(TestCSP.valuesVariants(TestBoard, (row, col))) + ","

    #         assert TestCSP.valuesVariants(TestBoard, (row, col)) == \
    #                TestGlobals.valuesVariants_answerHB()[row * boardDim+ col], "valuesVariants failed for HB"
    print "test valuesVariants passed"

    # test allValuesVariants
    assert TestCSP.allValuesVariants(TestBoard) == \
                   TestGlobals.valuesVariants_answerHB(), "allvaluesVariants failed for HB"
    print "test allValuesVariants passed"

    # test MRV
    # print TestCSP.MRV(TestBoard)
    assert TestCSP.MRV(TestBoard) == (7, 6), "MVR failed for HB"
    print "test MVR passed"

# run test
CSPtest()