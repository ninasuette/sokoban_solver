# A node is a data structure constituting part of a search tree
# includes parent, depth, path cost, action to reach
# node from parent of node, a description of the state
import copy
from Level import Level
# from sokoban import Search

# possibleMoves = {'R': [1, 0], 'L': [-1, 0], 'U': [0, -1],  'D': [0, 1]}
possibleMoves = ([1, 0], [-1, 0], [0, -1], [0, 1])


class Node(object):

    def __init__(self, parent, matrix, action, costs):
        self.parent = parent
        self.matrix = matrix
        self.action = action
        self.costs = costs

    # the function generates all possible nodes from the actual node
    def expand(self):

        states = []
        # {'R': [1, 0], 'L': [-1, 0], 'U': [0, -1],  'D': [0, 1]}
        for event in possibleMoves:
            moved_matrix = copy.deepcopy(self.matrix)
            possible_move = self.possible_move(moved_matrix, event[0], event[1]) or self.possible_push(moved_matrix, event[0], event[1])

            if possible_move:

                self.movePlayer(moved_matrix,event)
                s = Node(self, moved_matrix, event, 1)
                states.append(s)
        return states

    # reached goal node
    def goal(self):
        return self.is_completed()

    # checks if complete
    def is_completed(self):
        for row in self.matrix:
            for cell in row:
                if cell == '$':
                    return False
        return True

    def next(self, matrix, x, y):
        current_position = self.getPlayerPosition(matrix)
        return self.get_content(matrix, current_position[0] + x, current_position[1] + y)

    # checks if pushing the box is possible
    def possible_push(self, matrix, x, y):
        return self.next(matrix, x, y) in ['*', '$'] and self.next(matrix, x + x, y + y) in [' ', '.']

    def get_content(self, matrix, x, y):
        return matrix[y][x]

    # checks if move leads to wall
    def possible_move(self, matrix, x, y):
        current_position = self.getPlayerPosition(matrix)
        # print(self.current_position[0]+x)
        # print(self.current_position[1]+y)
        return self.get_content(matrix, current_position[0] + x, current_position[1] + y) not in ['#', '*', '$']

    def getPlayerPosition(self, matrix):
        # Iterate all Rows
        for i in range(0, len(matrix)):
            # Iterate all columns
            for k in range(0, len(matrix[i]) - 1):
                if matrix[i][k] == "@":
                    return [k, i]

    def movePlayer(self, moved_matrix,  direction):
        # matrix = self.getMatrix()


        x = self.getPlayerPosition(moved_matrix)[0]
        y = self.getPlayerPosition(moved_matrix)[1]

        target_found = False

        # print boxes

        if direction == [-1, 0]:
            # print("######### Moving Left #########")

            # if is_space
            if moved_matrix[y][x - 1] == " ":
                # print("OK Space Found")
                moved_matrix[y][x - 1] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                    target_found = False
                else:
                    moved_matrix[y][x] = " "

            # if is_box
            elif moved_matrix[y][x - 1] == "$":
                # print("Box Found")
                if moved_matrix[y][x - 2] == " ":
                    moved_matrix[y][x - 2] = "$"
                    moved_matrix[y][x - 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "
                elif moved_matrix[y][x - 2] == ".":
                    moved_matrix[y][x - 2] = "*"
                    moved_matrix[y][x - 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "


            # if is_box_on_target
            elif moved_matrix[y][x - 1] == "*":
                # print("Box on target Found")
                if moved_matrix[y][x - 2] == " ":
                    moved_matrix[y][x - 2] = "$"
                    moved_matrix[y][x - 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

                elif moved_matrix[y][x - 2] == ".":
                    moved_matrix[y][x - 2] = "*"
                    moved_matrix[y][x - 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif moved_matrix[y][x - 1] == ".":
                # print("Target Found")
                moved_matrix[y][x - 1] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                else:
                    moved_matrix[y][x] = " "
                target_found = True

            # else
            #else:
                # print("There is a wall here")

        elif direction == [1, 0]:
            # print("######### Moving Right #########")

            # if is_space
            if moved_matrix[y][x + 1] == " ":
                # print("OK Space Found")
                moved_matrix[y][x + 1] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                    target_found = False
                else:
                    moved_matrix[y][x] = " "

            # if is_box
            elif moved_matrix[y][x + 1] == "$":
                # print("Box Found")
                if moved_matrix[y][x + 2] == " ":
                    moved_matrix[y][x + 2] = "$"
                    moved_matrix[y][x + 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

                elif moved_matrix[y][x + 2] == ".":
                    moved_matrix[y][x + 2] = "*"
                    moved_matrix[y][x + 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

            # if is_box_on_target
            elif moved_matrix[y][x + 1] == "*":
                # print("Box on target Found")
                if moved_matrix[y][x + 2] == " ":
                    moved_matrix[y][x + 2] = "$"
                    moved_matrix[y][x + 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

                elif moved_matrix[y][x + 2] == ".":
                    moved_matrix[y][x + 2] = "*"
                    moved_matrix[y][x + 1] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif moved_matrix[y][x + 1] == ".":
                # print("Target Found")
                moved_matrix[y][x + 1] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                else:
                    moved_matrix[y][x] = " "
                target_found = True

            # else
            #else:
                # print("There is a wall here")

        elif direction == [0, 1]:
            # print("######### Moving Down #########")

            # if is_space
            if moved_matrix[y + 1][x] == " ":
                # print("OK Space Found")
                moved_matrix[y + 1][x] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                    target_found = False
                else:
                    moved_matrix[y][x] = " "

            # if is_box
            elif moved_matrix[y + 1][x] == "$":
                # print("Box Found")
                if moved_matrix[y + 2][x] == " ":
                    moved_matrix[y + 2][x] = "$"
                    moved_matrix[y + 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

                elif moved_matrix[y + 2][x] == ".":
                    moved_matrix[y + 2][x] = "*"
                    moved_matrix[y + 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

            # if is_box_on_target
            elif moved_matrix[y + 1][x] == "*":
                # print("Box on target Found")
                if moved_matrix[y + 2][x] == " ":
                    moved_matrix[y + 2][x] = "$"
                    moved_matrix[y + 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

                elif moved_matrix[y + 2][x] == ".":
                    moved_matrix[y + 2][x] = "*"
                    moved_matrix[y + 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif moved_matrix[y + 1][x] == ".":
                # print("Target Found")
                moved_matrix[y + 1][x] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                else:
                    moved_matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")

        elif direction == [0, -1]:
            # print("######### Moving Up #########")

            # if is_space
            if moved_matrix[y - 1][x] == " ":
                # print("OK Space Found")
                moved_matrix[y - 1][x] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                    target_found = False
                else:
                    moved_matrix[y][x] = " "

            # if is_box
            elif moved_matrix[y - 1][x] == "$":
                # print("Box Found")
                if moved_matrix[y - 2][x] == " ":
                    moved_matrix[y - 2][x] = "$"
                    moved_matrix[y - 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

                elif moved_matrix[y - 2][x] == ".":
                    moved_matrix[y - 2][x] = "*"
                    moved_matrix[y - 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                        target_found = False
                    else:
                        moved_matrix[y][x] = " "

            # if is_box_on_target
            elif moved_matrix[y - 1][x] == "*":
                # print("Box on target Found")
                if moved_matrix[y - 2][x] == " ":
                    moved_matrix[y - 2][x] = "$"
                    moved_matrix[y - 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

                elif moved_matrix[y - 2][x] == ".":
                    moved_matrix[y - 2][x] = "*"
                    moved_matrix[y - 1][x] = "@"
                    if target_found == True:
                        moved_matrix[y][x] = "."
                    else:
                        moved_matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif moved_matrix[y - 1][x] == ".":
                # print("Target Found")
                moved_matrix[y - 1][x] = "@"
                if target_found == True:
                    moved_matrix[y][x] = "."
                else:
                    moved_matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")