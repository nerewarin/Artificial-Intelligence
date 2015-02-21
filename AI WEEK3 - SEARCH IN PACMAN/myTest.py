__author__ = 'NereWARin'
import pacman
from game import GameStateData
from game import Game
from game import Directions
from game import Actions
from util import nearestPoint
from util import manhattanDistance
import util, layout
# import sys, types, time, random, os
#
# argv = "-l tinyMaze -p SearchAgent"
# args = readCommand( sys.argv[1:] )
# pacman.runGames( **args )
# python pacman.py -l tinyMaze -p SearchAgent
# python pacman.py -l mediumMaze -p SearchAgent
# python pacman.py -l bigMaze -z .5 -p SearchAgent

lst = [((2, 5), 'West', 1), ((2, 5), 'East', 1), ((4, 5), 'West', 1), ((1, 5), 'West', 1), \
       ((3, 5), 'East', 1), ((3, 5), 'West', 1)]


def sortBy1(inputStr):
        return inputStr[0]

# lst.sort(key=sortBy1)
# lst.sort(key=lambda x: x[0])
lst.sort()
print lst
 # key=lambda x: x[::-1])

print len( ['West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'South', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'West', 'West', 'South', 'South', 'North', 'North', 'East', 'East', 'East', 'East', 'North', 'North', 'East'] )