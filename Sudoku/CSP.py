__author__ = 'NereWARin'
# import Board
import TestGlobals, time # , operator
from Board import SudokuBoard

class CSP():
    # def __init__(self, numbers = range(1, 10)):
    #     self.numbers = numbers



    def BacktrackingSearch(self, board, impossibleTag = "Failure"):
        # precompute -- first we check correctness of task
        # Then, initialize variants in every cell and sort it as a dictionary
        # where key = number of possible variants (lenght of list),
        # value = list of cells with appropriate variants lenght
        InitialCheck = board.preCompute()
        if InitialCheck != "Task checked OK":
            print InitialCheck
            return board
        # run algorithm
        return self.RecursiveBacktracking(board, impossibleTag)

    def RecursiveBacktracking(self, board, impossibleTag = "Failure"):
        """
        recursive solution search
        :param board: input board
        :param impossibleTag: defines answer that function returns if search cannot find solution
        :return: complete board or "Failure"
        """
        if board.isFull():
            print "SUCCESSFULLY RESOLVED!"
            return board
        # select unassigned variable

        # MRV version
        cell, variants = board.MRV()
        for var in variants:
            mBoard =  board.copy()
            mBoard.setAndUpdate(cell, var)
            result = self.RecursiveBacktracking(mBoard, impossibleTag)
            if result != impossibleTag:
                return result
            # print "backup UndefinedSymbol in cell", cell
            mBoard.clearAndUpdate(cell)
            return impossibleTag

        # # MRV + LCV version
        # for pair in board.MRVandLCV():
        #     cell, var = pair
        #     # if var == "no more variants":
        #     #     return impossibleTag
        #     mBoard =  board.copy()
        #     mBoard.setAndUpdate(cell, var)
        #     result = self.RecursiveBacktracking(mBoard, impossibleTag)
        #     if result != impossibleTag:
        #         return result
        #     # print "backup UndefinedSymbol in cell", cell
        #     mBoard.clearAndUpdate(cell)
        #     return impossibleTag

def CSPtest():
    # test BacktrackingSearch
    TestCSP = CSP()

    # test boards
    print "initialize test boards"
    TestBoard         = SudokuBoard(TestGlobals.definedNubmers_HB())
    TestCompleteBoard = SudokuBoard(TestGlobals.definedNubmers_COMPLETE())
    TestEasyBoard     = SudokuBoard(TestGlobals.definedNubmers_EB())
    TestHB2           = SudokuBoard(TestGlobals.definedNubmers_HB2())



    print "\nBacktrackingSearch HB"
    start_time = time.time()
    answerHB = TestCSP.BacktrackingSearch(TestBoard)
    print answerHB
    # assert answerHB.checkAll() == ({}, {}, {}), "incorrect HardBoard solution"
    print "time to compute =",time.time() - start_time

    print "\nBacktrackingSearch EasyBoard"
    start_time = time.time()
    answerEB = TestCSP.BacktrackingSearch(TestEasyBoard)
    print answerEB
    assert answerEB.checkAll() == ({}, {}, {}), "incorrect EasyBoard solution"
    print "time to compute =",time.time() - start_time

    print "\nBacktrackingSearch HB2"
    start_time = time.time()
    answerHB2 = TestCSP.BacktrackingSearch(TestHB2)
    print answerHB2
    # assert answerHB2.checkAll() == ({}, {}, {}), "incorrect HB2 solution"
    print "time to compute =",time.time() - start_time

    print "\nBacktrackingSearch INCORRECT_COMPLETE"
    asnwerINCORRECT_COMPLETE = TestCSP.BacktrackingSearch(TestCompleteBoard)
    assert asnwerINCORRECT_COMPLETE.checkAll() == TestGlobals.conflicts4x4_board(), "incorrect asnwerINCORRECT_COMPLETE checkall"
    # print asnwerINCORRECT_COMPLETE

    # # 4x4 test
    # Test4x4         = SudokuBoard(TestGlobals._4x4_board(), "x", range(1, 17))
    # print "\nBacktrackingSearch answerTest4x4"
    # start_time = time.time()
    # answerTest4x4 = TestCSP.BacktrackingSearch(Test4x4)
    # print answerTest4x4
    # assert answerTest4x4.checkAll() == ({}, {}, {}), "incorrect answerTest4x4 solution"
    # print "time to compute =",time.time() - start_time

    print "\npassed test CSP"
# run test
if __name__ == "__main__":
    CSPtest()

