__author__ = 'NereWARin'
import CSP, Board

class TestCSP(Board.SudokuBoard):
    """
    test class
    """
    def __init__(self):
        self.board = self.HardBoard()
        self.csp = CSP.CSP()

    def HardBoard(self):
        definedNubmers = {(0,0):8,
                      (1,2):3, (1,3):6,
                      (2,1):7,(2,4):9, (2,6):2,
                      (3,1):5, (3,5):7,
                      (4,4):4, (4,5):5, (4,6):7,
                      (5,3):1, (5,7):3,
                      (6,2):1, (6,7):8, (6,8):6,
                      (7,2):8, (7,3):5, (7,7):1,
                      (8,1):9, (8,6):4      }
        return Board.SudokuBoard(definedNubmers)

    def test_valuesVariants(self):
        def answersHB():
            return [[8],
                    [0, 1, 2, 4, 6],
                    [0, 2, 4, 5, 6, 9],
                    [0, 2, 3, 4, 7],
                    [0, 1, 2, 3, 5, 7],
                    [0, 1, 2, 3, 4],
                    [0, 1, 3, 5, 6, 9],
                    [0, 4, 5, 6, 7, 9],
                    [0, 1, 3, 4, 5, 7, 9],
                    [0, 1, 2, 4, 5, 9],
                    [0, 1, 2, 4],
                    [3],
                    [6],
                    [0, 1, 2, 5, 7, 8],
                    [0, 1, 2, 4, 8],
                    [0, 1, 5, 8, 9],
                    [0, 4, 5, 7, 9],
                    [0, 1, 4, 5, 7, 8, 9],
                    [0, 1, 4, 5, 6],
                    [7],
                    [0, 4, 5, 6],
                    [0, 3, 4, 8],
                    [9],
                    [0, 1, 3, 4, 8],
                    [2],
                    [0, 4, 5, 6],
                    [0, 1, 3, 4, 5, 8],
                    [0, 1, 2, 3, 4, 6, 9],
                    [5],
                    [0, 2, 4, 6, 9],
                    [0, 2, 3, 8, 9],
                    [0, 2, 3, 6, 8],
                    [7],
                    [0, 1, 6, 8, 9],
                    [0, 2, 4, 6, 9],
                    [0, 1, 2, 4, 8, 9],
                    [0, 1, 2, 3, 6, 9],
                    [0, 1, 2, 3, 6, 8],
                    [0, 2, 6, 9],
                    [0, 2, 3, 8, 9],
                    [4],
                    [5],
                    [7],
                    [0, 2, 6, 9],
                    [0, 1, 2, 8, 9],
                    [0, 2, 4, 6, 7, 9],
                    [0, 2, 4, 6, 8],
                    [0, 2, 4, 6, 7, 9],
                    [1],
                    [0, 2, 6, 8],
                    [0, 2, 6, 8, 9],
                    [0, 5, 6, 8, 9],
                    [3],
                    [0, 2, 4, 5, 8, 9],
                    [0, 2, 3, 4, 5, 7],
                    [0, 2, 3, 4],
                    [1],
                    [0, 2, 3, 4, 7, 9],
                    [0, 2, 3, 7],
                    [0, 2, 3, 4, 9],
                    [0, 3, 5, 9],
                    [8],
                    [6],
                    [0, 2, 3, 4, 6, 7],
                    [0, 2, 3, 4, 6],
                    [8],
                    [5],
                    [0, 2, 3, 6, 7],
                    [0, 2, 3, 4, 6, 9],
                    [0, 3, 9],
                    [1],
                    [0, 2, 3, 7, 9],
                    [0, 2, 3, 5, 6, 7],
                    [9],
                    [0, 2, 5, 6, 7],
                    [0, 2, 3, 7, 8],
                    [0, 1, 2, 3, 6, 7, 8],
                    [0, 1, 2, 3, 6, 8],
                    [4],
                    [0, 2, 5, 7],
                    [0, 2, 3, 5, 7]]

        TestBoard = self.copy()
        TestCSP = self.csp
        # TestCSP.valuesVariants(TestBoard, (0,1))
        for row in range(TestBoard.getBoardDim()):
            for col in range(TestBoard.getBoardDim()):
                # print (row, col), TestCSP.valuesVariants(TestBoard, (row, col))
                print str(TestCSP.valuesVariants(TestBoard, (row, col))) + ","

# print "hello Test Test"