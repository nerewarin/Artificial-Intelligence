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

    start_state =  problem.getStartState()
    start_successors = problem.getSuccessors(start_state)
    # print "Start:", start_state
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", start_successors

    fringe = util.Stack()
    for moving in start_successors:
        fringe.push( (moving[0], [moving[1]], moving[2]) )

    closed = [start_state]

    while not fringe.isEmpty():
        moving = fringe.pop()
        if problem.isGoalState(moving[0]):
            # print "RETURN ", moving[1]
            return moving[1]
        # print "moving: ", moving#, "go to", moving[0]
        closed.append(moving[0])
        # print "closed: %s" % closed
        successors = problem.getSuccessors(moving[0])
        # print "sorted successors", successors
        for child in successors:
            if child[0] not in closed:
                # print "push %s" % str(child)
                fringe.push( (child[0], moving[1]+ [child[1]], child[2]) )
    else:
        print "Failure!"
        return []
    # insert these as arguments for pacman.py for tests (run - edit configuration using PyCharm)
    # -l tinyMaze -p SearchAgent
    # -l mediumMaze -p SearchAgent
    # -l bigMaze -z .5 -p SearchAgent
    # autograder.py arguments: -q q1


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_state =  problem.getStartState()
    start_successors = problem.getSuccessors(start_state)
    # print "Start:", start_state
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", start_successors

    fringe = util.Queue()
    pushed = set([])
    for moving in start_successors:
        # print type(moving), moving
        # fringe.push( (moving[0], [moving[1]], moving[2]) )
        fringe.push( moving )
        pushed.add(moving[0])
    closed = [start_state]

    while not fringe.isEmpty():
        moving = fringe.pop()
        if problem.isGoalState(moving[0]):
            print "RETURN ", moving[1]
            return moving[1]
        print "moving: ", moving#, "go to", moving[0]


        closed.append(moving[0])
        # print "closed: %s" % closed
        successors = problem.getSuccessors(moving[0])
        # print "sorted successors", successors
        for child in successors:
            # print "child[0]", child[0]
            if (child[0] not in closed) and (child[0] not in pushed):
                # print "push %s" % str(child)

                #  # add for corners problem
                # print "child", type(child), child, len(child)
                # if len(child) == 2: # add for corners problem
                #     not_vis_corners = child[1]
                #     child = child[0]
                #     moving  = moving[0]
                #     print "moving..", moving, moving[0]
                #     fringe.push( (child[0][0], moving[1] + [child[1]], child[2]), not_vis_corners )
                # else:
                #     fringe.push( (child[0], moving[1]+ [child[1]], child[2]) )
                #  # end add for corners problem
                fringe.push( (child[0], moving[1]+ [child[1]], child[2]) )
                pushed.add(child[0])
    else:
        print "Failure!"
        return []
    # insert these as arguments for pacman.py for tests (run - edit configuration using PyCharm)
    # -l mediumMaze -p SearchAgent -a fn=bfs
    # -l bigMaze -p SearchAgent -a fn=bfs -z .5
    # autograder.py arguments: -q q2

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state =  problem.getStartState()
    start_successors = problem.getSuccessors(start_state)
    successors = {start_state : start_successors}
    # print "Start:", start_state
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", start_successors

    fringe = util.PriorityQueue()
    pushed = set([])
    best_cost = {}
    for moving in start_successors:
        # print "push", ( (moving[0], [moving[1]], moving[2]) , moving[2])
        # print "push", ( moving[0], [moving[1]], moving[2])
        fringe.push( (moving[0], [moving[1]], moving[2]) , moving[2])
        best_cost[moving[0]] = moving[2]
        # pushed.add(moving[0])
        pushed.add(moving)
    # closed = [(start_state, "", 0)]
    closed = [start_state]

    while not fringe.isEmpty():
        moving = fringe.pop()
        if problem.isGoalState(moving[0]):
            # print "RETURN ", moving[1]
            return moving[1]
        # print "moving to %s %s" % (moving[0],  moving)#, "go to", moving[0]
        closed.append(moving[0])
        # print "closed: %s" % closed
        if moving[0] not in successors.keys(): # the main change is to define a dict
            successors[moving[0]] = problem.getSuccessors(moving[0])
        # else:
        #     delta =  best_cost[moving[0]] - moving[2]
        #     if delta:
        #         # update cost of current moving
        #         best_cost[moving[0]] = moving[2]
        #         # update costs of future movings
        #         new_sucs = []
        #         print "HERE uccessors[moving[0]", successors[moving[0]]
        #         for successor in successors[moving[0]]:
        #             print "successor", successor
        #             print "successor[1]", successor[1]
        #             new_sucs.append( (successor[0],
        #                               moving[1] + successor[1][-1], # update move vs current plus move to suc
        #                               successor[2] - delta ))
        #         successors[moving[0]] = new_sucs
        # print "moving: %s closed: %s sorted successors: %s" % (moving, closed , successors)
        for child in successors[moving[0]]:
            # print "child[0]", child[0]
            if (child[0] not in closed) and (child not in pushed):
                best_cost[child[0]] = moving[2] + child[2]
                # print "push", (child[0], moving[1] + [child[1]], moving[2] + child[2]), moving[2] + child[2]
                fringe.push( (child[0], moving[1] + [child[1]], moving[2] + child[2]), moving[2] + child[2] )
                pushed.add(child)
    else:
        print "Failure!"
        return []
    # insert these as arguments for pacman.py for tests (run - edit configuration using PyCharm)

    # autograder.py arguments: -q q3

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    start_state =  problem.getStartState()
    start_successors = problem.getSuccessors(start_state)
    successors = {start_state : start_successors}

    # succ_heur = []
    # for successor in start_successors:
    #     # succ_heur.append(successor[2] + heuristic(successor, problem) )
    #     print "successor[2]", successor[2]



    # Hn = heuristic(start_state, problem)


    # successors = {start_state : (start_successors[0], start_successors[1], start_successors[2] + heuristic(start_state, problem) )  }


    # print "Start:", start_state
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", start_successors
    # print "heuristic func = ", heuristic
    # print "heuristic start_state", heuristic(start_state, problem)
    # print "succ_Fn", succ_Fn

    # print "successors dict",  successors[start_state]


    # succ_Fn = [(successor[2] + heuristic(successor[0], problem)) for successor in start_successors]
    # for successor in start_successors:
    #
    # successors = {start_state : (start_successors[0], start_successors[1], start_successors[2] + heuristic(start_state, problem) )  }
    #
    # return []

    fringe = util.PriorityQueue()
    pushed = set([])
    best_cost = {}
    for moving in start_successors:
        # print "push", ( (moving[0], [moving[1]], moving[2]) , moving[2])
        # print "push", ( moving[0], [moving[1]], moving[2])

         # A*
        succ_Fn =  moving[2] + heuristic(moving[0], problem) #
        # print "push moving", moving, "with succ_Fn =", succ_Fn
        fringe.push( (moving[0], [moving[1]], moving[2]) , succ_Fn) #
        best_cost[moving[0]] = succ_Fn #
        # pushed.add(moving[0])
        pushed.add(moving)
    # closed = [(start_state, "", 0)]
    closed = [start_state]

    # print "loop"
    while not fringe.isEmpty():
        moving = fringe.pop()
        if problem.isGoalState(moving[0]):
            # print "RETURN ", moving[1]
            return moving[1]
        # print "moving to %s %s" % (moving[0],  moving)#, "go to", moving[0]
        closed.append(moving[0])
        # print "closed: %s" % closed
        if moving[0] not in successors.keys():
            successors[moving[0]] = problem.getSuccessors(moving[0])
        for child in successors[moving[0]]:
            succ_Fn =  moving[2] + child[2] + heuristic(child[0], problem) #
            # succ_Fn =  moving[2]  + heuristic(child[0], problem) #
            # print "child", child,  "with succ_Fn =", succ_Fn
            if (child[0] not in closed) and (child not in pushed):
                # best_cost[child[0]] = moving[2] + child[2]
                best_cost[child[0]] = succ_Fn #
                # print "push", (child[0], moving[1] + [child[1]], moving[2] + child[2]), moving[2] + child[2]
                fringe.push( (child[0], moving[1] + [child[1]], moving[2] + child[2]), succ_Fn )
                pushed.add(child)
    else:
        print "Failure!"
        return []

    # insert these as arguments for pacman.py for tests (run - edit configuration using PyCharm)
    # -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    # autograder.py arguments: -q q4


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
