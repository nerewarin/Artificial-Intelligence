__author__ = 'NereWARin'

"""
Constants parameters of board that are used for tests
"""

def definedNubmers_HB():
    """
    Hard board from HardBoard.jpg -- the most difficult Sudoku 2015
    :return:
    """
    definedNubmers = {(0,0):8,
                  (1,2):3, (1,3):6,
                  (2,1):7,(2,4):9, (2,6):2,
                  (3,1):5, (3,5):7,
                  (4,4):4, (4,5):5, (4,6):7,
                  (5,3):1, (5,7):3,
                  (6,2):1, (6,7):6, (6,8):8,
                  (7,2):8, (7,3):5, (7,7):1,
                  (8,1):9, (8,6):4      }
    return definedNubmers


def definedNubmers_EB(o = "x"):
    """
    easy board from http://www.soduko.org/sudoku-print.php?id=1000000000
    : param o : undefinedSymbol
    :return:
    """
    definedNubmers =[[o, o, o, o, 2 , o, 7, o , o],
                     [8, o, o, 3, o , o, 9, o , o],
                     [o, o, 6, o, o , 5, o, o , 1],
                     [4, o, o, 8, 7 , o, o, 2 , o],
                     [o, 9, o, 1, o , o, o, 3 , o],
                     [o, 5, o, o, 6 , o, o, o , 4],
                     [7, o, o, 9, o , o, 5, o , o],
                     [o, o, 1, o, o , 6, o, o , 8],
                     [o, o, 5, o, 4 , o, o, o , o]]
    return definedNubmers

def definedNubmers_HB2(o = "x"):
    """
    hard board from Yulia (uppedr-middle difficult)    https://vk.com/im?peers=c14&sel=11278110&z=photo11278110_365177766%2Fmail15930
    : param o : undefinedSymbol
    :return:
    """
    return [[o, 7, o, o, o, o, 6, o, o],
            [6, 2, o, o, 9, 1, o, o, 8],
            [o, 8, o, 5, o, 6, o, o, 2],
            [o, 5, o, 6, o, 3, o, 2, o],
            [o, o, o, o, o, o, o, o, o],
            [o, 9, o, 8, o, 2, o, 6, o],
            [9, o, 8, o, o, 7, o, 3, o],
            [4, o, o, 1, 6, o, o, 8, 7],
            [7, o, 5, o, o, o, o, 4, o]]

def definedNubmers_COMPLETE():
    """
    incorrectly complete board
    :return:
    """
    definedNubmers = {}
    for row in range(9):
        for col in range(9):
            definedNubmers[(row, col)] = ((row + col * 3) ) % 9 + 1
    return definedNubmers


# ANSWERS FOR TESTS
def valuesVariants_answerHB():
    # return [[8], [1, 2, 4, 6], [2, 4, 5, 6, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 6, 9], [4, 5, 7, 9], [1, 3, 4, 5, 6, 7, 9], [1, 2, 4, 5, 9], [1, 2, 4], [3], [6], [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9], [1, 4, 5, 6], [7], [4, 5, 6], [3, 4, 8], [9], [1, 3, 4, 8], [2], [4, 5, 8], [1, 3, 4, 5, 6], [1, 2, 3, 4, 6, 9], [5], [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], [7], [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9], [1, 2, 3, 6, 9], [1, 2, 3, 6, 8], [2, 6, 9], [2, 3, 8, 9], [4], [5], [7], [2, 8, 9], [1, 2, 6, 9], [2, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 7, 9], [1], [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], [3], [2, 4, 5, 6, 9], [2, 3, 4, 5, 7], [2, 3, 4], [1], [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], [6], [8], [2, 3, 4, 6, 7], [2, 3, 4, 6], [8], [5], [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], [1], [2, 3, 7, 9], [2, 3, 5, 6, 7], [9], [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], [4], [2, 5, 7], [2, 3, 5, 7]]
    # return [[[8], [1, 2, 4, 5, 9], [1, 4, 5, 6], [1, 2, 3, 4, 6, 9], [1, 2, 3, 6, 9], [2, 4, 6, 7, 9], [2, 3, 4, 5, 7], [2, 3, 4, 6, 7], [2, 3, 5, 6, 7]],
    #         [[1, 2, 4, 6], [1, 2, 4], [7], [5], [1, 2, 3, 6, 8], [2, 4, 6, 8], [2, 3, 4], [2, 3, 4, 6], [9]],
    #         [[2, 4, 5, 6, 9], [3], [4, 5, 6], [2, 4, 6, 9], [2, 6, 9], [2, 4, 6, 7, 9], [1], [8], [2, 5, 6, 7]],
    #         [[2, 3, 4, 7], [6], [3, 4, 8], [2, 3, 8, 9], [2, 3, 8, 9], [1], [2, 3, 4, 7, 9], [5], [2, 3, 7, 8]],
    #         [[1, 2, 3, 5, 7], [1, 2, 5, 7, 8], [9], [2, 3, 6, 8], [4], [2, 6, 8], [2, 3, 7], [2, 3, 6, 7], [1, 2, 3, 6, 7, 8]],
    #         [[1, 2, 3, 4], [1, 2, 4, 8], [1, 3, 4, 8], [7], [5], [2, 6, 8, 9], [2, 3, 4, 9], [2, 3, 4, 6, 9], [1, 2, 3, 6, 8]],
    #         [[1, 3, 5, 6, 9], [1, 5, 8, 9], [2], [1, 6, 8, 9], [7], [5, 6, 8, 9], [3, 5, 9], [3, 9], [4]],
    #         [[4, 5, 7, 9], [4, 5, 7, 8, 9], [4, 5, 8], [2, 4, 8, 9], [2, 8, 9], [3], [6], [1], [2, 5, 7]],
    #         [[1, 3, 4, 5, 6, 7, 9], [1, 4, 5, 7, 9], [1, 3, 4, 5, 6], [1, 2, 4, 6, 9], [1, 2, 6, 9], [2, 4, 5, 6, 9], [8], [2, 3, 7, 9], [2, 3, 5, 7]]]
    # return [[[8], [1, 2, 4, 6], [2, 4, 5, 6, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 6, 9], [4, 5, 7, 9], [1, 3, 4, 5, 6, 7, 9]],
    #     [[1, 2, 4, 5, 9], [1, 2, 4], [3], [6], [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]],
    #     [[1, 4, 5, 6], [7], [4, 5, 6], [3, 4, 8], [9], [1, 3, 4, 8], [2], [4, 5, 8], [1, 3, 4, 5, 6]],
    #     [[1, 2, 3, 4, 6, 9], [5], [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], [7], [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]],
    #     [[1, 2, 3, 6, 9], [1, 2, 3, 6, 8], [2, 6, 9], [2, 3, 8, 9], [4], [5], [7], [2, 8, 9], [1, 2, 6, 9]],
    #     [[2, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 7, 9], [1], [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], [3], [2, 4, 5, 6, 9]],
    #     [[2, 3, 4, 5, 7], [2, 3, 4], [1], [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], [6], [8]],
    #     [[2, 3, 4, 6, 7], [2, 3, 4, 6], [8], [5], [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], [1], [2, 3, 7, 9]],
    #     [[2, 3, 5, 6, 7], [9], [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], [4], [2, 5, 7], [2, 3, 5, 7]]]
    # in this version I changed filled numver to * to indicate that cell is full and has no another variants
    return [['*', [1, 2, 4, 6], [2, 4, 5, 6, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 6, 9], [4, 5, 7, 9], [1, 3, 4, 5, 6, 7, 9]], [[1, 2, 4, 5, 9], [1, 2, 4], '*', '*', [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]], [[1, 4, 5, 6], '*', [4, 5, 6], [3, 4, 8], '*', [1, 3, 4, 8], '*', [4, 5, 8], [1, 3, 4, 5, 6]], [[1, 2, 3, 4, 6, 9], '*', [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], '*', [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]], [[1, 2, 3, 6, 9], [1, 2, 3, 6, 8], [2, 6, 9], [2, 3, 8, 9], '*', '*', '*', [2, 8, 9], [1, 2, 6, 9]], [[2, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 7, 9], '*', [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], '*', [2, 4, 5, 6, 9]], [[2, 3, 4, 5, 7], [2, 3, 4], '*', [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], '*', '*'], [[2, 3, 4, 6, 7], [2, 3, 4, 6], '*', '*', [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], '*', [2, 3, 7, 9]], [[2, 3, 5, 6, 7], '*', [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], '*', [2, 5, 7], [2, 3, 5, 7]]]


def updateVariants_answerHB():
    """
    after (0,1) = 6
    :return:
    """
    # return [[8], [6], [2, 4, 5, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 9], [4, 5, 7, 9], [1, 3, 4, 5, 7, 9], [1, 2, 4, 5, 9], [1, 2, 4], [3], [6], [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9], [1, 4, 5], [7], [4, 5], [3, 4, 8], [9], [1, 3, 4, 8], [2], [4, 5, 8], [1, 3, 4, 5, 6], [1, 2, 3, 4, 6, 9], [5], [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], [7], [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9], [1, 2, 3, 6, 9], [1, 2, 3, 8], [2, 6, 9], [2, 3, 8, 9], [4], [5], [7], [2, 8, 9], [1, 2, 6, 9], [2, 4, 6, 7, 9], [2, 4, 8], [2, 4, 6, 7, 9], [1], [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], [3], [2, 4, 5, 6, 9], [2, 3, 4, 5, 7], [2, 3, 4], [1], [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], [6], [8], [2, 3, 4, 6, 7], [2, 3, 4], [8], [5], [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], [1], [2, 3, 7, 9], [2, 3, 5, 6, 7], [9], [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], [4], [2, 5, 7], [2, 3, 5, 7]]
    # return [[[8], [6], [2, 4, 5, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 9], [4, 5, 7, 9], [1, 3, 4, 5, 7, 9]], [[1, 2, 4, 5, 9], [1, 2, 4], [3], [6], [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]], [[1, 4, 5], [7], [4, 5], [3, 4, 8], [9], [1, 3, 4, 8], [2], [4, 5, 8], [1, 3, 4, 5, 6]], [[1, 2, 3, 4, 6, 9], [5], [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], [7], [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]], [[1, 2, 3, 6, 9], [1, 2, 3, 8], [2, 6, 9], [2, 3, 8, 9], [4], [5], [7], [2, 8, 9], [1, 2, 6, 9]], [[2, 4, 6, 7, 9], [2, 4, 8], [2, 4, 6, 7, 9], [1], [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], [3], [2, 4, 5, 6, 9]], [[2, 3, 4, 5, 7], [2, 3, 4], [1], [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], [6], [8]], [[2, 3, 4, 6, 7], [2, 3, 4], [8], [5], [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], [1], [2, 3, 7, 9]], [[2, 3, 5, 6, 7], [9], [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], [4], [2, 5, 7], [2, 3, 5, 7]]]
    return [['*', '*', [2, 4, 5, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 9], [4, 5, 7, 9], [1, 3, 4, 5, 7, 9]], [[1, 2, 4, 5, 9], [1, 2, 4], '*', '*', [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]], [[1, 4, 5], '*', [4, 5], [3, 4, 8], '*', [1, 3, 4, 8], '*', [4, 5, 8], [1, 3, 4, 5, 6]], [[1, 2, 3, 4, 6, 9], '*', [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], '*', [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]], [[1, 2, 3, 6, 9], [1, 2, 3, 8], [2, 6, 9], [2, 3, 8, 9], '*', '*', '*', [2, 8, 9], [1, 2, 6, 9]], [[2, 4, 6, 7, 9], [2, 4, 8], [2, 4, 6, 7, 9], '*', [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], '*', [2, 4, 5, 6, 9]], [[2, 3, 4, 5, 7], [2, 3, 4], '*', [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [3, 5, 9], '*', '*'], [[2, 3, 4, 6, 7], [2, 3, 4], '*', '*', [2, 3, 6, 7], [2, 3, 4, 6, 9], [3, 9], '*', [2, 3, 7, 9]], [[2, 3, 5, 6, 7], '*', [2, 5, 6, 7], [2, 3, 7, 8], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 8], '*', [2, 5, 7], [2, 3, 5, 7]]]

def updateVariants_answerHB_883():
    """
    after (8,8) = 3
    :return:
    """
    # return [[[8], [1, 2, 4, 6], [2, 4, 5, 6, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 6, 9], [4, 5, 7, 9], [1, 4, 5, 6, 7, 9]], [[1, 2, 4, 5, 9], [1, 2, 4], [3], [6], [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]], [[1, 4, 5, 6], [7], [4, 5, 6], [3, 4, 8], [9], [1, 3, 4, 8], [2], [4, 5, 8], [1, 4, 5, 6]], [[1, 2, 3, 4, 6, 9], [5], [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], [7], [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]], [[1, 2, 3, 6, 9], [1, 2, 3, 6, 8], [2, 6, 9], [2, 3, 8, 9], [4], [5], [7], [2, 8, 9], [1, 2, 6, 9]], [[2, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 7, 9], [1], [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], [3], [2, 4, 5, 6, 9]], [[2, 3, 4, 5, 7], [2, 3, 4], [1], [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [5, 9], [6], [8]], [[2, 3, 4, 6, 7], [2, 3, 4, 6], [8], [5], [2, 3, 6, 7], [2, 3, 4, 6, 9], [9], [1], [2, 7, 9]], [[2, 5, 6, 7], [9], [2, 5, 6, 7], [2, 7, 8], [1, 2, 6, 7, 8], [1, 2, 6, 8], [4], [2, 5, 7], [3]]]
    return [['*', [1, 2, 4, 6], [2, 4, 5, 6, 9], [2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 3, 4], [1, 3, 5, 6, 9], [4, 5, 7, 9], [1, 4, 5, 6, 7, 9]], [[1, 2, 4, 5, 9], [1, 2, 4], '*', '*', [1, 2, 5, 7, 8], [1, 2, 4, 8], [1, 5, 8, 9], [4, 5, 7, 8, 9], [1, 4, 5, 7, 9]], [[1, 4, 5, 6], '*', [4, 5, 6], [3, 4, 8], '*', [1, 3, 4, 8], '*', [4, 5, 8], [1, 4, 5, 6]], [[1, 2, 3, 4, 6, 9], '*', [2, 4, 6, 9], [2, 3, 8, 9], [2, 3, 6, 8], '*', [1, 6, 8, 9], [2, 4, 8, 9], [1, 2, 4, 6, 9]], [[1, 2, 3, 6, 9], [1, 2, 3, 6, 8], [2, 6, 9], [2, 3, 8, 9], '*', '*', '*', [2, 8, 9], [1, 2, 6, 9]], [[2, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 7, 9], '*', [2, 6, 8], [2, 6, 8, 9], [5, 6, 8, 9], '*', [2, 4, 5, 6, 9]], [[2, 3, 4, 5, 7], [2, 3, 4], '*', [2, 3, 4, 7, 9], [2, 3, 7], [2, 3, 4, 9], [5, 9], '*', '*'], [[2, 3, 4, 6, 7], [2, 3, 4, 6], '*', '*', [2, 3, 6, 7], [2, 3, 4, 6, 9], [9], '*', [2, 7, 9]], [[2, 5, 6, 7], '*', [2, 5, 6, 7], [2, 7, 8], [1, 2, 6, 7, 8], [1, 2, 6, 8], '*', [2, 5, 7], '*']]

def getAnswer_SolutionEB():
    return [[5, 1, 9, 6, 2, 8, 7, 4, 3],
            [8, 4, 2, 3, 1, 7, 9, 5, 6],
            [3, 7, 6, 4, 9, 5, 2, 8, 1],
            [4, 6, 3, 8, 7, 9, 1, 2, 5],
            [2, 9, 8, 1, 5, 4, 6, 3, 7],
            [1, 5, 7, 2, 6, 3, 8, 9, 4],
            [7, 3, 4, 9, 8, 1, 5, 6, 2],
            [9, 2, 1, 5, 3, 6, 4, 7, 8],
            [6, 8, 5, 7, 4, 2, 3, 1, 9]]

def getAnswer_SolutionHB():
    return [[8, 1, 2, 7, 5, 3, 6, 4, 9],
            [9, 4, 3, 6, 8, 2, 1, 7, 5],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [1, 5, 4, 2, 3, 7, 8, 9, 6],
            [3, 6, 9, 8, 4, 5, 7, 2, 1],
            [2, 8, 7, 1, 6, 9, 5, 3, 4],
            [5, 2, 1, 9, 7, 4, 3, 6, 8],
            [4, 3, 8, 5, 2, 6, 9, 1, 7],
            [7, 9, 6, 3, 1, 8, 4, 5, 2]]
