# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
#     Important note: Remember that a search node must contain not only a state
# but also the information necessary to reconstruct the path (plan) which gets to that state.
#
# Important note: All of your search functions need to return a list of actions that will lead
# the agent from the start to the goal. These actions all have to be legal moves (valid directions, no moving through walls).
#
# Important note: Make sure to use the Stack, Queue and PriorityQueue data structures
# provided to you in util.py! These data structure implementations have particular properties
# which are required for compatibility with the autograder.
#      caling from registerInitialState of searchAgents.py
    "*** YOUR CODE HERE ***"

    print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())#, "type of " , type(problem.getSuccessors(problem.getStartState()))

    # code providing pseudocode

    # fringe = problem.getSuccessors(problem.getStartState())
    fringe = util.Stack()
    # fringe.push(problem.getStartState())
    # for moving in problem.getSuccessors(problem.getStartState()):
    for moving in sorted(problem.getSuccessors(problem.getStartState()), reverse=True):
        # fringe.push(moving)
        fringe.push( (moving[0], [moving[1]], moving[2]) )

    closed = {}
    actions = []
    while not fringe.isEmpty():
        moving = fringe.pop()
        # if moving[0] in closed:
        if moving[0] in closed.keys():
            actions = closed[moving[0]]

        if problem.isGoalState(moving[0]):
            # actions.append( moving[1] )
            actions = moving[1]
            break
        # if moving not in closed:
        if moving[0] not in closed.keys():
            print "moving: ", moving#, "go to", moving[0]
            actions.append( moving[1] )
            # closed.add(moving[0])
            closed[moving[0]] = actions
            # print "sorted successors", sorted(problem.getSuccessors(moving[0]))
            print "sorted successors", sorted(problem.getSuccessors(moving[0]), reverse=True)
            # for child in sorted(problem.getSuccessors(moving[0])):
            deadend = True
            for child in sorted(problem.getSuccessors(moving[0]), reverse=True):
                # print "push %s" % str(child)
                # fringe.push(child)
                if child[0] not in closed:
                    print "push %s" % str(child)
                    fringe.push( (child[0], moving[1]+ [child[1]], child[2]) )
            if deadend:
                actions.pop()
        print "closed: %s" % closed
        # print "fringe: %s" % fringe
    else:
        print "Failure!"
        return []
    print "RETURN ", actions
    # insert these as arguments for pacman.py for tests (run - edit configuration using PyCharm)
    # -l tinyMaze -p SearchAgent
    # -l mediumMaze -p SearchAgent
    # -l bigMaze -z .5 -p SearchAgent
    return  actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
