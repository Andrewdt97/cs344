from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule
from random import randint
import copy

class State():
    def __init__(self, numCities, map):
        self.map = map
        self.path =[]
        # Initialize a full state solution
        for i in range( numCities ):
            self.path.append(i)

    def swap(self, action):
        temp = self.path[action[0]]
        self.path[action[0]] = self.path[action[1]]
        self.path[action[1]] = temp

    def calculateDistance(self):
        distance = 0
        for i in range( 1, len( self.path ) ):
            distance += self.map[ self.path[i] ][ self.path[i - 1] ]
        return distance


class TSP(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, numCities):
        self.initial = State( numCities, self.createMap( numCities ) )

    def actions(self, state):
        possibleActions = []
        # Find ten possible swaps
        for i in range(10):
            rand1 = randint( 0, len( state.path ) - 1 )
            rand2 = randint( 0, len( state.path ) - 1 )
            if rand1 != rand2:
                possibleActions.append( [ rand1, rand2 ])
        return possibleActions

    def result(self, state, action):
        newState = copy.deepcopy( state )
        newState.swap( action )
        return newState

    def value(self, state):
        return -1 * state.calculateDistance()

    def createMap(self, numCities):

        map = []
        # Initialize numCites x numCities array
        for i in range(numCities):
            map.append([None] * numCities)
        # Fill in half of the matrix while mirror across the middle axis
        for x in range(numCities):
            for y in range(numCities):
                if x >= y:
                    continue
                if x < y:
                    dist = randint(0, 100)
                    map[x][y] = dist
                    map[y][x] = dist
        # Print the map for fact checking
        for y in range(numCities):
            for x in range(numCities):
                print(map[x][y], end="\t\t")
            print()

        return map


if __name__ == '__main__':

    p = TSP(10)
    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    print('Hill-climbing solution       Path: ' + str(hill_solution.path)
          + '\tvalue: ' + str(p.value(hill_solution))
          )

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )

    print('Simulated annealing solution Path: ' + str( annealing_solution.path )
          + '\tvalue: ' + str(p.value(annealing_solution))
          )