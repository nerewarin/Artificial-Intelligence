__author__ = 'NereWARin'
import Board, TestGlobals

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
        cell, variants = self.MRV(board)

        for var in variants:
            # print cell, variants, var
            mBoard =  board.copy()
            mBoard.setValue(cell, var)

        # else:
            # TODO

def CSPtest():


    # test BacktrackingSearch
    print "BacktrackingSearch", TestCSP.BacktrackingSearch(TestBoard)

# run test
CSPtest()