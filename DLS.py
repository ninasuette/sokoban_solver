from node import Node
import collections
import time

# Equals to depth-first search with depth limit 𝑙 i.e. nodes at
# depth 𝑙 have no successors

class DLS():


    def __solution(self, node):
        if node == "F":
            return "Could not find a solution!", None
        if node == "C":
            return "Could not find a solution!", None

        actions = []
        while node.parent:
            actions.append(node.action)
            node = node.parent
        t1 = time.time()
        time_measure = t1 - t0
        return actions[::-1], time_measure

    def __depth(self, node):
        depth = 0
        parent = node.parent
        while parent:
            parent = parent.parent
            depth = depth + 1
        return depth

    def search(self, node:Node):
        records = {
            'node': 0,
            'repeat': 0,
            'fringe': 0,
            'explored': set([]),
            'limit': 6,
            'depth': 0
        }
        cutoff_occurred = False

        if node.goal():  # check if initial state is complete
            return node

        elif self.__depth(node) == records['limit']:
            return "C"

        else:
            for child_expansion in node.expand():
                result = self.search(child_expansion)
                records['depth'] = self.__depth(child_expansion)
                if result == "C":
                    cutoff_occurred = True
                elif result:
                    return result
            if cutoff_occurred:
                return "C"
            else:
                return "F"

    def search_algorithm(self, node: Node):
        global t0
        t0 = time.time()
        node = self.search(node)
        return self.__solution(node)


"""
    def __solution(self, child_expansion: Node):
        actions = []
        node = child_expansion
        while node.parent:
            actions.append(node.action)
            node = node.parent
        return actions[::-1]


    def search_algorithm(self, node: Node):
        records = {
        'node' : 0,
        'repeat' : 0,
        'fringe' : 0,
        'explored' : set([]),
        'depth' : 0,
        'limit' : 6
        }

        if node.goal():    # check if initial state is complete
            return records

        fringe = collections.deque()
        fringe.append(node)
        explored = []
        records['node'] += 1
        records['depth'] += 1

        while True:
            if not fringe: # fail if no options left
                print(records)
                return None

            node_board = fringe.pop()            # move to next node
            records['explored'].add(hash(node_board))   # add hash to explored
            records['fringe'] = len(fringe)
            explored.append(node_board)  # add the node explored

            if records['depth'] <= records['limit']:

                for child_expansion in node_board.expand():

                    records['node'] += 1
                    #
                    if hash(child_expansion) not in records['explored'] and child_expansion not in fringe:
                        if child_expansion.goal():  # if the board is solved
                            solution = self.__solution(child_expansion)
                            return solution

                        else:
                            fringe.append(child_expansion)
                            records['repeat'] += 1

            else: raise Exception('Limit reached. Solution not found.')
    """

