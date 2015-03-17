# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()

        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        # compute dist to closest ghost
        ghostDist = "inf"
        for ghostState in newGhostStates:
            # print type(ghostState), dir(ghostState)
            # <type 'instance'>
            # ['__doc__', '__eq__', '__hash__', '__init__', '__module__', '__str__', 'configuration',
            # 'copy', 'getDirection', 'getPosition', 'isPacman', 'numCarrying', 'numReturned', 'scaredTimer', 'start']
            ghostDist =  min(ghostDist, manhattanDistance(newPos, ghostState.getPosition()))
        penalty = 0
        if ghostDist < 2:
            penalty = 1000


        # compute dist to closest food
        foodDist = 1000
        for food in newFood.asList():
            # print type(newFood), dir(newFood)
            #<type 'instance'>
            # ['CELLS_PER_INT', '__doc__', '__eq__', '__getitem__', '__hash__', '__init__', '__module__',
            # '__setitem__', '__str__', '_cellIndexToPosition', '_unpackBits', '_unpackInt',
            # 'asList', 'copy', 'count', 'data', 'deepCopy', 'height', 'packBits', 'shallowCopy', 'width']
            # print "food", food
            foodDist = min(foodDist, manhattanDistance(newPos, food))


        # print newScaredTimes
        # return successorGameState.getScore()  + sum(newScaredTimes) #+ 1/foodDist
        # return successorGameState.getScore()  +  1.0/newFood.count()
        # return 0.1*ghostDist - newFood.count()
        # return ghostDist - 2*foodDist
        return successorGameState.getScore() - penalty - 0.01*foodDist
        # return 0.5*(ghostDist - foodDist) + successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game

          gameState.isWin():
            Returns whether or not the game state is a winning state

          gameState.isLose():
            Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # print "func_name evaluationFunction", self.evaluationFunction.func_name
        print "gameState.getNumAgents()", gameState.getNumAgents()

        # pacActions =  gameState.getLegalActions(0)
        # ghost1Actions = gameState.getLegalActions(1)
        # ghost2Actions = gameState.getLegalActions(2)
        # print "self.evaluationFunction", self.evaluationFunction
        # print "dir self.evaluationFunction", dir(self.evaluationFunction)
        # ['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
        #  '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__',
        # '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
        #  '__sizeof__', '__str__', '__subclasshook__',
        # 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']

        # print "pacActions = %s ,ghost1Actions = %s , ghost2Actions = %s " % (pacActions, ghost1Actions, ghost2Actions)
        # print "self.evaluationFunction(gameState)", self.evaluationFunction(gameState)
        # state = gameState
        # ancestors = [("root", 0, gameState)] #      0 = pacman
        # tree = {ancestor : {"" : state} }

        # fringe = util.Queue()
        # fringe.push(
        # closed = [start_state]

        # # initialization
        # tree = {}
        # ancestor_states = [gameState]
        # acts_states = [("nth0", "nth1")]
        # print dir(gameState) # = ['__doc__', '__eq__', '__hash__', '__init__', '__module__', '__str__',
        # # 'data', 'deepCopy', 'explored', 'generatePacmanSuccessor', 'generateSuccessor', 'getAndResetExplored',
        # # 'getCapsules', 'getFood', 'getGhostPosition', 'getGhostPositions', 'getGhostState', 'getGhostStates',
        # # 'getLegalActions', 'getLegalPacmanActions', 'getNumAgents', 'getNumFood', 'getPacmanPosition',
        # # 'getPacmanState', 'getScore', 'getWalls', 'hasFood', 'hasWall', 'initialize', 'isLose', 'isWin']
        #
        # agents_states = []
        # # for agent_num in xrange(gameState.getNumAgents()):
        # # agents_states.append(gameState.getPacmanPosition)
        # # print "PacmanPosition", gameState.getPacmanPosition()
        # # print "GhostPositions", gameState.getGhostPositions()
        # # for agent_num in xrange(gameState.getNumAgents() - 1):
        # #     print gameState.getGhostPositions
        # # pacActions =  gameState.getLegalActions(0)
        # # ghost1Actions = gameState.getLegalActions(1)
        # # ghost2Actions = gameState.getLegalActions(2)
        # # ancestors = ["root"]
        def min_value(agent, state, remaining_depth):
            # best_act, best_score  = None, self.evaluationFunction(gameState)
            best_score = float("inf")
            successors = [state.generateSuccessor(agent, action) for action in state.getLegalActions(agent)]
            nextAgent = (agent + 1) % state.getNumAgents()
            # print "min_value nextAgent", nextAgent, "sucs_num = ", len(successors)
            for suc in successors:
                best_score = min(best_score, mm_value(nextAgent, suc, remaining_depth))
                # print "min_value local best_score", best_score
            return best_score

        def max_value(agent, state, remaining_depth):
            # best_act, best_score  = None, self.evaluationFunction(gameState)
            best_score = float("-inf")
            successors = [state.generateSuccessor(agent, action) for action in state.getLegalActions(agent)]
            nextAgent = (agent + 1) % state.getNumAgents()
            # print "max_value nextAgent", nextAgent
            for suc in successors:
                best_score = max(best_score, mm_value(nextAgent, suc, remaining_depth))
            return best_score

        def mm_value(agent, state, remaining_depth):
            # print "mm_value agent", agent, "remdepth", remaining_depth
            if (state.isWin() or state.isLose() or not remaining_depth):
                # print "win?", state.isWin(), "lose?", state.isLose(), "score =", self.evaluationFunction(state)
                return self.evaluationFunction(state)
            if agent:
                return min_value(agent, state, remaining_depth)
            # else Pacman
            return max_value(agent, state, remaining_depth-1)

        pacActions =  gameState.getLegalActions(0)
        scores = {}
        for action in pacActions:
            scores[action] = mm_value(1, gameState.generateSuccessor(0, action), self.depth)
        print scores
        # find max score
        # best_act, best_score  = None, self.evaluationFunction(gameState)
        # print "(0 > -inf?)", 0.0 > float("-inf")
        best_act, best_score  = None, float("-inf")
        for act, value in scores.iteritems():
            # print "act, value, best_score", act, value, best_score
            if value > best_score:
                # print "new best_score"
                best_act = act
                best_score = value
        print "best_act", best_act, "best_score", best_score
        return best_act


        print "\nSTART"
        for ply in xrange(self.depth):
            for agent_num in xrange(gameState.getNumAgents()):
                print "ply, agent = ", ply, agent_num
                # for action in ancestor_state.getLegalActions(agent_num):
                # maybe check win here?
                # tree[(ply, agent_num, ancestor_state)] = []
                for pre_state in ancestor_states:
                    sucStates = [pre_state.generateSuccessor(agent_num, action) for action in pre_state.getLegalActions(agent_num)]
                    tree[(ply, agent_num, pre_state)] = sucStates
                    # acts_states = [(action, pre_state.generateSuccessor(agent_num, action)) for action in pre_state.getLegalActions(agent_num)]
                    ## key = (ply, agent_num, pre_state), value = (action, successor_state)
                    # tree[(ply, agent_num, pre_state)] = acts_states
                # ancestor_states = [state[1] for state in  acts_states]
                ancestor_states = [state for state in sucStates]

        # for key, value in tree.iteritems():
        #     actions = []
        #     for action, state in value:
        #         actions.append(action)
        #     print "ply %s agent %s : %s " % (key[0], key[1], actions)
        print tree
        # for ply in xrange(self.depth, 0, -1):
        #     for agent_num in xrange(gameState.getNumAgents(), 0, -1):
        #         print tree[(ply, agent_num, pre_state)]

        # # build tree of actions-states
        # for ply in xrange(self.depth):
        #     # actions = [state.getLegalActions(agent_num) for agent_num in xrange(state.getNumAgents())]
        #     # print "actions", actions
        #     #
        #     # # compute minimax
        #     # score = "-inf"
        #     # # # pacman step
        #     # for pacAction in actions[0]:
        #     #     print "pacAction", pacAction
        #     #     state = gameState.generateSuccessor(0, pacAction)
        #     # universal cycle but..who min who max?...
        #     for agent_num in xrange(gameState.getNumAgents()):
        #         # for _key_, _state_ in tree[ancestor].iteritems():
        #         #     for action in _state_.getLegalActions(agent_num):
        #         #         print "action", action
        #         #         new_state = _state_.generateSuccessor(agent_num, action)
        #         # for ancestor in ancestors:
        #         #     for action in ancestor[2].getLegalActions(agent_num):
        #         for action in
        #
        #     # call evaluation function
        #     # self.evaluationFunction(state)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

