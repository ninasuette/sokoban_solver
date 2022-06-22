
import pygame
from Level import Level
import copy

class Search(object):

    def __init__(self, environment, theme, level_set):
        self.myEnvironment = environment
        self.theme = theme
        self.level_set = level_set
        self.matrix_history = []

    def drawLevel(self, matrix_to_draw):
        # Load level images
        wall = pygame.image.load(self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/wall.png').convert()
        box = pygame.image.load(self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/box.png').convert()
        box_on_target = pygame.image.load(
            self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/box_on_target.png').convert()
        space = pygame.image.load(self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/space.png').convert()
        target = pygame.image.load(self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/target.png').convert()
        player = pygame.image.load(self.myEnvironment.getPath() + '/themes/' + self.theme + '/images/player.png').convert()

        # If horizontal or vertical resolution is not enough to fit the level images then resize images
        if self.getSize()[0] > self.myEnvironment.size[0] / 36 or self.getSize()[1] > self.myEnvironment.size[1] / 36:

            # If level's x size > level's y size then resize according to x axis
            if self.getSize()[0] / self.getSize()[1] >= 1:
                new_image_size = self.myEnvironment.size[0] / self.getSize()[0]
            # If level's y size > level's x size then resize according to y axis
            else:
                new_image_size = self.myEnvironment.size[1] / self.getSize()[1]

            # Just to the resize job
            wall = pygame.transform.scale(wall, (new_image_size, new_image_size))
            box = pygame.transform.scale(box, (new_image_size, new_image_size))
            box_on_target = pygame.transform.scale(box_on_target, (new_image_size, new_image_size))
            space = pygame.transform.scale(space, (new_image_size, new_image_size))
            target = pygame.transform.scale(target, (new_image_size, new_image_size))
            player = pygame.transform.scale(player, (new_image_size, new_image_size))

        # Just a Dictionary (associative array in pyhton's lingua) to map images to characters used in level design
        images = {'#': wall, ' ': space, '$': box, '.': target, '@': player, '*': box_on_target}

        # Get image size. Images are always squares so it doesn't care if you get width or height
        box_size = wall.get_width()

        # Iterate all Rows
        for i in range(0, len(matrix_to_draw)):
            # Iterate all columns of the row
            for c in range(0, len(matrix_to_draw[i])):
                self.myEnvironment.screen.blit(images[matrix_to_draw[i][c]], (c * box_size, i * box_size))

        pygame.display.update()

    def initLevel(self, level_set, level):
        # Create an instance of this Level
        global myLevel
        myLevel = Level(level_set, level)
        self.matrix = myLevel.getMatrix()
        # Draw this level
        # self.drawLevel(self.matrix)

        global target_found
        target_found = False

    def movePlayer(self, direction):
        # matrix = self.getMatrix()
        self.matrix = self.matrix
        self.addToHistory(self.matrix)

        x = self.getPlayerPosition()[0]
        y = self.getPlayerPosition()[1]

        global target_found

        # print boxes
        # print(self.getBoxes())

        if direction == [-1, 0]:
            # print("######### Moving Left #########")

            # if is_space
            if self.matrix[y][x - 1] == " ":
                # print("OK Space Found")
                self.matrix[y][x - 1] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                    target_found = False
                else:
                    self.matrix[y][x] = " "

            # if is_box
            elif self.matrix[y][x - 1] == "$":
                # print("Box Found")
                if self.matrix[y][x - 2] == " ":
                    self.matrix[y][x - 2] = "$"
                    self.matrix[y][x - 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "
                elif self.matrix[y][x - 2] == ".":
                    self.matrix[y][x - 2] = "*"
                    self.matrix[y][x - 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "


            # if is_box_on_target
            elif self.matrix[y][x - 1] == "*":
                # print("Box on target Found")
                if self.matrix[y][x - 2] == " ":
                    self.matrix[y][x - 2] = "$"
                    self.matrix[y][x - 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

                elif self.matrix[y][x - 2] == ".":
                    self.matrix[y][x - 2] = "*"
                    self.matrix[y][x - 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif self.matrix[y][x - 1] == ".":
                # print("Target Found")
                self.matrix[y][x - 1] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                else:
                    self.matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")

        elif direction == [1, 0]:
            # print("######### Moving Right #########")

            # if is_space
            if self.matrix[y][x + 1] == " ":
                # print("OK Space Found")
                self.matrix[y][x + 1] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                    target_found = False
                else:
                    self.matrix[y][x] = " "

            # if is_box
            elif self.matrix[y][x + 1] == "$":
                # print("Box Found")
                if self.matrix[y][x + 2] == " ":
                    self.matrix[y][x + 2] = "$"
                    self.matrix[y][x + 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

                elif self.matrix[y][x + 2] == ".":
                    self.matrix[y][x + 2] = "*"
                    self.matrix[y][x + 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

            # if is_box_on_target
            elif self.matrix[y][x + 1] == "*":
                # print("Box on target Found")
                if self.matrix[y][x + 2] == " ":
                    self.matrix[y][x + 2] = "$"
                    self.matrix[y][x + 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

                elif self.matrix[y][x + 2] == ".":
                    self.matrix[y][x + 2] = "*"
                    self.matrix[y][x + 1] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif self.matrix[y][x + 1] == ".":
                # print("Target Found")
                self.matrix[y][x + 1] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                else:
                    self.matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")

        elif direction == [0, 1]:
            # print("######### Moving Down #########")

            # if is_space
            if self.matrix[y + 1][x] == " ":
                # print("OK Space Found")
                self.matrix[y + 1][x] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                    target_found = False
                else:
                    self.matrix[y][x] = " "

            # if is_box
            elif self.matrix[y + 1][x] == "$":
                # print("Box Found")
                if self.matrix[y + 2][x] == " ":
                    self.matrix[y + 2][x] = "$"
                    self.matrix[y + 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

                elif self.matrix[y + 2][x] == ".":
                    self.matrix[y + 2][x] = "*"
                    self.matrix[y + 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

            # if is_box_on_target
            elif self.matrix[y + 1][x] == "*":
               # print("Box on target Found")
                if self.matrix[y + 2][x] == " ":
                    self.matrix[y + 2][x] = "$"
                    self.matrix[y + 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

                elif self.matrix[y + 2][x] == ".":
                    self.matrix[y + 2][x] = "*"
                    self.matrix[y + 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif self.matrix[y + 1][x] == ".":
                # print("Target Found")
                self.matrix[y + 1][x] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                else:
                    self.matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")

        elif direction == [0, -1]:
            # print("######### Moving Up #########")

            # if is_space
            if self.matrix[y - 1][x] == " ":
                # print("OK Space Found")
                self.matrix[y - 1][x] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                    target_found = False
                else:
                    self.matrix[y][x] = " "

            # if is_box
            elif self.matrix[y - 1][x] == "$":
                # print("Box Found")
                if self.matrix[y - 2][x] == " ":
                    self.matrix[y - 2][x] = "$"
                    self.matrix[y - 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

                elif self.matrix[y - 2][x] == ".":
                    self.matrix[y - 2][x] = "*"
                    self.matrix[y - 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                        target_found = False
                    else:
                        self.matrix[y][x] = " "

            # if is_box_on_target
            elif self.matrix[y - 1][x] == "*":
                # print("Box on target Found")
                if self.matrix[y - 2][x] == " ":
                    self.matrix[y - 2][x] = "$"
                    self.matrix[y - 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

                elif self.matrix[y - 2][x] == ".":
                    self.matrix[y - 2][x] = "*"
                    self.matrix[y - 1][x] = "@"
                    if target_found == True:
                        self.matrix[y][x] = "."
                    else:
                        self.matrix[y][x] = " "
                    target_found = True

            # if is_target
            elif self.matrix[y - 1][x] == ".":
                # print("Target Found")
                self.matrix[y - 1][x] = "@"
                if target_found == True:
                    self.matrix[y][x] = "."
                else:
                    self.matrix[y][x] = " "
                target_found = True

            # else
            # else:
                # print("There is a wall here")

        self.drawLevel(self.matrix)

        # print("Boxes remaining: " + str(len(self.getBoxes())))

        if len(self.getBoxes()) == 0:
            self.myEnvironment.screen.fill((0, 0, 0))
            # print("Level Completed")
            global current_level
            current_level = 0
            current_level += 1
            self.initLevel(self.level_set, current_level)

    def get_content(self, x, y):
        return self.matrix[y][x]

    # checks if move leads to wall
    def possible_move(self, x, y):
        self.current_position = self.getPlayerPosition()
        # print(self.current_position[0]+x)
        # print(self.current_position[1]+y)
        return self.get_content(self.current_position[0] + x, self.current_position[1] + y) not in ['#', '*', '$']

    def next(self, x, y):
        self.current_position = self.getPlayerPosition()
        return self.get_content(self.current_position[0] + x, self.current_position[1] + y)

    # checks if pushing the box is possible
    def possible_push(self, x, y):
        return self.next(x, y) in ['*', '$'] and self.next(x + x, y + y) in [' ', '.']

    def getMatrix(self):
        return self.matrix

    def addToHistory(self, matrix):
        self.matrix_history.append(copy.deepcopy(self.matrix))

    def getLastMatrix(self):
        if len(self.matrix_history) > 0:
            lastMatrix = self.matrix_history.pop()
            self.matrix = lastMatrix
            return lastMatrix
        else:
            return self.matrix

    def getPlayerPosition(self):
        # Iterate all Rows
        for i in range(0, len(self.matrix)):
            # Iterate all columns
            for k in range(0, len(self.matrix[i]) - 1):
                if self.matrix[i][k] == "@":
                    return [k, i]

    def getBoxes(self):
        # Iterate all Rows
        boxes = []
        for i in range(0, len(self.matrix)):
            # Iterate all columns
            for k in range(0, len(self.matrix[i]) - 1):
                if self.matrix[i][k] == "$":
                    boxes.append([k, i])
        return boxes

    def getSize(self):
        max_row_length = 0
        # Iterate all Rows
        for i in range(0, len(self.matrix)):
            # Iterate all columns
            row_length = len(self.matrix[i])
            if row_length > max_row_length:
                max_row_length = row_length
        return [max_row_length, len(self.matrix)]

