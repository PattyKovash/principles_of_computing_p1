"""
Solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move

Run code in www.codeskultptor.org
July 2016 - PK
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.game = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.game = list(configuration)
        self.game.reverse()
            
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.game)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.game[len(self.game) - 1 - house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for i in range(len(self.game) - 1):
            if self.game[i] != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if (house_num == 0) or (self.get_num_seeds(house_num) == 0):
            return False
        elif self.get_num_seeds(house_num) == house_num:
            return True
        else:
            return False
   
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for i in range(len(self.game) - house_num, len(self.game)):
                self.game[len(self.game) - 1 - house_num] = 0
                self.game[i] += 1
        else:
            return "That is not a valid move. Please try again."
    
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for i in range(len(self.game) - 2, -1, -1):
            house_num = len(self.game) - 1 - i
            if self.is_legal_move(house_num):
                return house_num
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves = []
        holder = list(self.game)        
        while self.choose_move():
            house_num = self.choose_move()
            moves.append(house_num)
            self.apply_move(house_num)
        self.game = holder
        return moves    
    
# Create tests to check the correctness of your code

#def test_mancala():
#    """
#    Test code for Solitaire Mancala
#    """
#    
#    my_game = SolitaireMancala()
#    my_game_2 = SolitaireMancala()
#    my_game_3 = SolitaireMancala()
#    print "Testing init - Computed:", my_game, "Expected: [0]"
#    
#    config1 = [0, 0, 1, 1, 3, 5, 0]  
#    config2 = [0, 0, 0, 0, 0]
#    config3 = [0,3,6,3]
#    my_game.set_board(config1)   
#    my_game_2.set_board(config2)
#    my_game_3.set_board(config3)
#
#    print my_game
#    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
#    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
#    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
#    print "Testing is_game_won - Computed:", my_game_2.is_game_won(), "Expected:", True
#    print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected:", False
#    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", True
#    print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected:", False
#    print "Testing is_legal_move - Computed:", my_game_3.is_legal_move(1), "Expected:", False
#    print "Testing is_legal_move - Computed:", my_game_3.is_legal_move(3), "Expected:", True
#    my_game.apply_move(5)
#    print "Testing apply_move - Computed:", my_game, "Expected:", str([0, 0, 4, 2, 2, 1, 1])
#    print "Testing apply_move - Computed:", my_game.apply_move(5), "Expected:", "That is not a valid move. Please try again."
#    my_game_3.apply_move(3)
#    print "Testing apply_move - Computed:", my_game_3, "Expected:", str([0, 7, 4, 1])
#    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
#    print "Testing choose_move - Computed:", my_game_2.choose_move(), "Expected:", 0
#    print "Testing choose_move - Computed:", my_game_3.choose_move(), "Expected:", 0
#    print "Testing plan_move - Computed:", my_game.plan_moves(), "Expected:", [1, 2, 1, 4, 1, 3, 1, 2, 1]
    
#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala()) 

import user41_c1Y8sBmMOa_8 as poc_mancala_testsuite
poc_mancala_testsuite.run_suite(SolitaireMancala)


