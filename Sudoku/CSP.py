__author__ = 'NereWARin'
# import Board
import TestGlobals, time # , operator
from Board import SudokuBoard

class CSP():
    # def __init__(self, numbers = range(1, 10)):
    #     self.numbers = numbers



    def BacktrackingSearch(self, board, impossibleTag = "Failure"):
        """
        recursive solution search
        :param board: input board
        :param impossibleTag: defines answer that function returns if search cannot find solution
        :return: complete board or "Failure"
        """
        if board.isFull():
            return board
        # select unassigned variable
        cell, variants = board.MRV()
        for var in variants:
            mBoard =  board.copy()
            mBoard.setAndUpdate(cell, var)
            result = self.BacktrackingSearch(mBoard, impossibleTag)
            if result != impossibleTag:
                return result
            # print "backup UndefinedSymbol in cell", cell
            mBoard.clearAndUpdate(cell)
        return impossibleTag

def CSPtest():
    # test boards
    print "initialize test boards"
    TestBoard         = SudokuBoard(TestGlobals.definedNubmers_HB())
    # TestCompleteBoard = SudokuBoard(TestGlobals.definedNubmers_COMPLETE())
    # TestEasyBoard     = SudokuBoard(TestGlobals.definedNubmers_EB())
    # TestHB2           = SudokuBoard(TestGlobals.definedNubmers_HB2())

    # test BacktrackingSearch
    TestCSP = CSP()

    print "BacktrackingSearch HB"
    start_time = time.time()
    answerHB = TestCSP.BacktrackingSearch(TestBoard)
    print answerHB
    assert answerHB.checkAll() == ({}, {}, {}), "incorrect HardBoard solution"
    print "time to compute =",time.time() - start_time


    # print "BacktrackingSearch Easy Board"
    # easySolution =  TestCSP.BacktrackingSearch(TestEasyBoard)
    # easySolution.checkAll()
    # print easySolution

    # print "BacktrackingSearch HB2"
    # hb2 = TestCSP.BacktrackingSearch(TestHB2)
    # print hb2

# run test
CSPtest()