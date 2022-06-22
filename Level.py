import os
import copy


class Level:
    matrix = []
    matrix_history = []

    def __init__(self, set, level_num):

        del self.matrix[:]
        del self.matrix_history[:]

        # Create level
        with open(os.path.dirname(os.path.abspath(__file__)) + '/levels/' + set + '/level' + str(level_num), 'r') as f:
            for row in f.read().splitlines():
                self.matrix.append(list(row))

    def getMatrix(self):
        return self.matrix

    def __del__(self):
        "Destructor to make sure object shuts down, etc."

