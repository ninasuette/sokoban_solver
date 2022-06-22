from node import Node
import collections
from copy import deepcopy
import time
# depth first search - expands deepest unexpanded node
# fringe ist last in first out
# put successors at front, but check
# new states against those at path from current node to root

class DFS():

    def __solution(self, child_expansion: Node):
        actions = []
        node = child_expansion
        while node.parent:
            actions.append(node.action)
            node = node.parent
        t1 = time.time()
        time_measure = t1-t0
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

        fringe = collections.deque()
        fringe.append(node)
        records['node'] += 1

        # das problem ist, dass immer die selben states genommen werden, daher springt er immer hin und her
        # endlos

        while fringe:

            node_board = fringe.pop()            # move to next node

            if node_board.goal():  # check if state is complete
                solution = self.__solution(node_board)
                return solution

            records['fringe'] = len(fringe)

            for child_expansion in node_board.expand():
                exists = False
                records['node'] += 1
                parent = child_expansion.parent
                compare_child = " ".join([" ".join(symbol) for symbol in child_expansion.matrix])
                while parent:
                    compare_parent = " ".join([" ".join(symbol) for symbol in parent.matrix])
                    if compare_child == compare_parent:
                        exists = True
                        break
                    parent = parent.parent
                if not exists:
                    fringe.append(child_expansion)
        return None




