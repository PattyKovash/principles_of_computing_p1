"""
Clone of 2048 game.
Run code in www.codeskulptor.com

Coursera - Rice University
Principles of Computing Part 1
July 2016 - PK
"""

import poc_2048_gui
import random

# Uncomment line 211 to play with GUI

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    merged = list(line)
    zeros = [0] * merged.count(0)
    
    # separate 0's & non-zero
    while 0 in merged:
        merged.pop(merged.index(0))

    # iterate non-zero list      
    for indx in range(len(merged)):
        # check to see if reached end of list
        if (indx + 1) != len(list(merged)):
            # if the current element == the next element,
            # multiply current element by 2, remove neighboring
            # element
            if merged[indx] == merged[indx + 1]:
                added = merged[indx] * 2
                merged[indx] = added
                merged.pop(indx + 1)
                merged.append(0)
    merged.extend(zeros)
    return merged

def get_line(start, direction, steps, grid):
    """
    Takes start indices of the input grid. Traverses grid
    in direction of input direction. Returns an array of 
    elements at each input index
    """
    line = []
    for ind in range(steps):
        row = start[0] + ind * direction[0]
        col = start[1] + ind * direction[1]
        line.append(grid[row][col])
    return line
        
def more_moves(grid, search):
    """
    Traverses grid. Returns True if search is found
    in grid.
    """
    for line in grid:
        if search in line:
            return True
    return False

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializes board to input width and height. 
        Stores board width and height.
        """
        self._height = grid_height
        self._width = grid_width
        self._board = []
        self.reset()
        self._more_moves = more_moves(self._board, 0)
        self._start_indx = {UP: [(0, indx * 1) for indx in range(self.get_grid_width())],
                            RIGHT: [(indx, self.get_grid_width() - 1) for indx in range(self.get_grid_height())],
                            DOWN: [(self.get_grid_height() - 1, indx * 1) for indx in range(self.get_grid_width())],
                            LEFT: [(indx * 1, 0) for indx in range(self.get_grid_height())]}
              
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_row in range(self._width)]
                      for dummy_column in range(self._height)]
        self.new_tile()
        self.new_tile()
       
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._board)
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
    
    def get_start_indx(self):
        """
        Returns start indices for each direction
        """
        return self._start_indx
    
    def get_more_moves(self):
        """
        Gets boolean value of more_moves
        """
        return self._more_moves
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        starting_ind = self.get_start_indx()[direction]
        offset_val = OFFSETS[direction]
        steps = self.get_grid_width()
        if direction == UP or direction == DOWN:
            steps = self.get_grid_height() 
        moved = False
        for ind in starting_ind:
            cur_line = get_line(ind, offset_val, steps, self._board)
            new_line = merge(cur_line)
            if cur_line != new_line:
                moved = True
            self.transpose(ind, offset_val, new_line)
        if moved and self.get_more_moves():
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        init_tiles = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        
        # randomly select board row, column , and tile value
        tile_row = random.randrange(self._height)
        tile_col = random.randrange(self._width)
        tile_val = random.choice(init_tiles)
        
        # check to see if selected tile already has a non-zero value
        while self._board[tile_row][tile_col] != 0:
            tile_row = random.randrange(self._height)
            tile_col = random.randrange(self._width)
            
        # reassign tile value
        self.set_tile(tile_row, tile_col, tile_val)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]
    
    def transpose(self, start, direction, line):
        """
        Traverses a grid along the provided start index and direction.
        replaces element at each index with element from input line.
        """
        for ind, elem in enumerate(list(line)):
            row = start[0] + ind * direction[0]
            col = start[1] + ind * direction[1]
            self._board[row][col] = elem

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#import user41_esNnZqJyCv_60 as poc_2048_testsuite
#poc_2048_testsuite.run_suite(TwentyFortyEight)
    
    
    



    
    


