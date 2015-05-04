__author__ = 'NereWARin'
import Board

class CSP():
    def __init__(self, numbers = 10):
        self.numbers = numbers

    def getNumbers(self):
        return self.numbers

    def valuesVariants(self, board, cell):
        if not board.isEmpty(cell):
            return [board.getValue(cell)]
        variants = range(self.getNumbers())
        result = []
        for value in variants:
            brd = board.copy()
            brd.setValue(cell, value)
            print "cell", cell, "var", value, brd.checkAll(cell)
            problems = False
            for problem in  brd.checkAll(cell):
            # if  brd.checkAll(cell) != ({}, {}, {}):
                if problem: problems = True
            if not problems:
                result.append(value)
        return result

def CSPtest():
    definedNubmers = {(0,0):8,
                      (1,2):3, (1,3):6,
                      (2,1):7,(2,4):9, (2,6):2,
                      (3,1):5, (3,5):7,
                      (4,4):4, (4,5):5, (4,6):7,
                      (5,3):1, (5,7):3,
                      (6,2):1, (6,7):8, (6,8):6,
                      (7,2):8, (7,3):5, (7,7):1,
                      (8,1):9, (8,6):4      }
    TestBoard    =    Board.SudokuBoard(definedNubmers)
    TestCSP = CSP()
    print TestCSP.valuesVariants(TestBoard, (0,3))
    # TestCSP.valuesVariants(TestBoard, (0,1))
    # for row in range(TestBoard.getBoardDim()):
    #     for col in range(TestBoard.getBoardDim()):
    #         print (row, col), TestCSP.valuesVariants(TestBoard, (row, col))

# run test
CSPtest()