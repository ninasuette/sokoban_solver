# Name: pySokoban
# Description: A sokoban implementation using python & pyGame
# Author: Kazantzakis Nikos <kazantzakisnikos@gmail.com>
# Date: 2015
# Last Modified: 31-03-2016
# https://github.com/kazantzakis/pySokoban
import copy
import argparse
import pygame
from Environment import Environment
from Search import Search
from BFS import BFS
from DFS import DFS
from DLS import DLS
from node import Node
import time

if __name__ == '__main__':

    # commandline interpreter
    # python sokoban.py -choose
    parser = argparse.ArgumentParser(description="Sokoban game")
    parser.add_argument("search_algorithm", help="Choose between 'bfs', 'dfs' and 'dls'")
    parser.add_argument("level", help="Choose a level")
    args = parser.parse_args()

    # Create the environment
    myEnvironment = Environment()

    # Choose a theme
    theme = "default"

    # Choose a level set
    level_set = "original"

    # Set the start Level
    # current_level = 2
    current_level = str(args.level)

    # Initialize Level
    pygame.init()

    search = Search(environment=myEnvironment, theme=theme, level_set=level_set)

    search.initLevel(level_set=level_set, level=current_level)
    matrix_copy = copy.deepcopy(search.matrix)
    node = Node(None, matrix_copy, 0, 0)

    bfs = BFS()
    dfs = DFS()
    dls = DLS()

    if str(args.search_algorithm) == 'bfs':
        solution, time_measure = bfs.search_algorithm(node)
    elif str(args.search_algorithm) == 'dfs':
        solution, time_measure = dfs.search_algorithm(node)
    elif str(args.search_algorithm) == 'dls':
        solution, time_measure = dls.search_algorithm(node)

    if not solution:
        print("No solution found.")
    else:
        solution_moves = []
        for step in solution:
            if step == [1, 0]:
                solution_moves.append('Move Right')
            elif step == [-1, 0]:
                solution_moves.append('Move Left')
            elif  step == [0, 1]:
                solution_moves.append('Move Down')
            elif step == [0, -1]:
                solution_moves.append('Move Up')

        print(solution)
        print(solution_moves)
        print(time_measure)

        # going the solution-steps
        for step in solution:
            search.movePlayer(step)
            time.sleep(0.6)
        time.sleep(5)

    """
    target_found = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    search.movePlayer("L", myLevel)
                elif event.key == pygame.K_RIGHT:
                    search.movePlayer("R", myLevel)
                elif event.key == pygame.K_DOWN:
                    search.movePlayer("D", myLevel)
                elif event.key == pygame.K_UP:
                    search.movePlayer("U", myLevel)
                elif event.key == pygame.K_u:
                    search.drawLevel(myLevel.getLastMatrix())
                elif event.key == pygame.K_r:
                    search.initLevel(level_set, current_level)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
"""
