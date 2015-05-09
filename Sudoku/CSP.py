__author__ = 'NereWARin'
# import Board
import TestGlobals, operator, time
from Board import SudokuBoard

class CSP():
    def __init__(self, numbers = range(1, 10)):
        self.numbers = numbers



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
        print "BacktrackingSearch get MVR"
        cell, variants = board.MRV()
        print "cell, variants", cell, variants
        # if cell == (None, None):
        #     print "fuck"

        # # try every var to order
        # var_count = {}
        # for var in variants:
        #     count = board.updateVariants(cell, var, "ordering")
        #     print var, count, variants
        #     var_count[var] = count
        # # sorting
        # # variants = sorted(var_count.keys(), key=var_count.values())
        # variants = sorted(var_count.items(), key=operator.itemgetter(1))
        # print "SORTING WORK????", variants

        # # row version (slow 08.05 day)
        # for var in variants:
        #     # print "assign var %s from variants %s in cell %s" % (var, variants, cell )
        #     mBoard =  board.copy()
        #     # mBoard.setValue(cell, var)
        #     # mBoard.updateVariants(cell, var)
        #     mBoard.setAndUpdate(cell, var)
        #     result = self.BacktrackingSearch(mBoard, impossibleTag)
        #     if result != impossibleTag:
        #         return result
        #     mBoard.setAndUpdate(cell, board.getUndefinedSymbol())
        # return impossibleTag

        # row version (slow 08.05 day)
        for var in variants:
            print "assign var %s from variants %s in cell %s" % (var, variants, cell )
            mBoard =  board.copy()
            # mBoard.setValue(cell, var)
            # mBoard.updateVariants(cell, var)
            mBoard.setAndUpdate(cell, var)
            result = self.BacktrackingSearch(mBoard, impossibleTag)
            if result != impossibleTag:
                return result
            print "backup UndefinedSymbol in cell", cell
            mBoard.setAndUpdate(cell, board.getUndefinedSymbol())
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
    # boardDim = TestBoard.getBoardDim()
    # for row in range(boardDim):
    #     for col in range(boardDim):
    #         print (row, col), TestCSP.valuesVariants(TestBoard, (row, col))#, TestGlobals.valuesVariants_answerHB()[row*boardDim + col]
            # print str(TestCSP.valuesVariants(TestBoard, (row, col))) + ","

    #         assert TestCSP.valuesVariants(TestBoard, (row, col)) == \
    #                TestGlobals.valuesVariants_answerHB()[row * boardDim+ col], "valuesVariants failed for HB"

    print "BacktrackingSearch HB"
    start_time = time.time()
    answerHB = TestCSP.BacktrackingSearch(TestBoard)
    print answerHB
    assert answerHB == TestGlobals.getAnswer_SolutionHB(), "unknown solution HB"
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