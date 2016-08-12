"""
Template testing suite for 2048
"""

import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def traverse_grid(start, direction, steps, grid):
    for step in range(steps):
        row = (start[0] + step) * direction[0]
        col = (start[1] + step) * direction[1]
        return grid[row][col]

def run_suite(board_class):
    """
    Testing for 2048 game
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a board
    board1 = board_class(2, 4)
    board2 = board_class(4, 5)
    board3 = board_class(5, 3)
    
    board2.set_tile(0, 0, 8)
    board2.set_tile(0, 1, 16)
    board2.set_tile(0, 2, 8)
    board2.set_tile(0, 3, 16)
    board2.set_tile(0, 4, 8)
    board2.set_tile(1, 0, 16)
    board2.set_tile(1, 1, 8)
    board2.set_tile(1, 2, 16)
    board2.set_tile(1, 3, 8)
    board2.set_tile(1, 4, 16)
    board2.set_tile(2, 0, 8)
    board2.set_tile(2, 1, 16)
    board2.set_tile(2, 2, 8)
    board2.set_tile(2, 3, 16)
    board2.set_tile(2, 4, 8)
    board2.set_tile(3, 0, 16)
    board2.set_tile(3, 1, 8)
    board2.set_tile(3, 2, 16)
    board2.set_tile(3, 3, 8)
    board2.set_tile(3,4,16)
    print "board2: ", board2
    print "start_ind: ", board2.get_start_indx()
    board2.move(DOWN)
    print board2
    
    # test the initial configuration of the board using the str method
    suite.run_test(board1.get_grid_height(), 2, "Test #0: get_grid_height")
    suite.run_test(board1.get_grid_width(), 4, "Test #1: get_grid_width")
    board1.set_tile(0, 3, 8)
    suite.run_test(board1.get_tile(0,3), 8, "Test #2: get_tile")
    


    # check the str and get_num_seeds methods
#    config1 = [0, 0, 1, 1, 3, 5, 0]    
#    game.set_board(config1)   
#    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
#    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
#    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
#    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")    
    
    # report number of tests and failures
    suite.report_results()
