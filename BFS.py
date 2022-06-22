from node import Node
import collections
from copy import deepcopy
import time

# Breadth-first search - expands shallowest unexpanded node
# fringe is first in first out
# new successors go at end


class BFS():
    def __solution(self, child_expansion:Node):
        actions = []
        node = child_expansion
        while node.parent:
            actions.append(node.action)
            node = node.parent
        t1 = time.time()
        time_measure = t1 - t0
        return actions[::-1], time_measure

    def search_algorithm(self, node: Node):
        global t0
        t0 = time.time()

        records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set([])
        }

        if node.goal():    # check if initial state is complete
            return self.__solution(node)

        fringe = collections.deque()
        fringe.appendleft(node)
        explored = []
        records['node'] += 1

        while True:
            if not fringe: # fail if no options left
                print(records)
                return None

            node_board = fringe.pop()            # move to next node
            records['explored'].add(hash(node_board))   # add hash to explored
            records['fringe'] = len(fringe)
            explored.append(node_board)  # add the node explored

            for child_expansion in node_board.expand():

                records['node'] += 1
                if hash(child_expansion) not in records['explored'] and child_expansion not in fringe:
                    if child_expansion.goal():  # if the board is solved
                        solution = self.__solution(child_expansion)
                        return solution
                    # else: fringe.appendleft(child_expansion)

                    else:
                        fringe.appendleft(child_expansion)
                        records['repeat'] += 1