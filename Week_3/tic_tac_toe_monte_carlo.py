"""
Coursera
Rice University
Principles of Computing Part 1

Monte Carlo Tic-Tac-Toe Player
Run code in www.codeskulptor.org

Implementation by PK
August 2016
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0   # Score for squares played by the current player
SCORE_OTHER = 1.0     # Score for squares played by the other player

def mc_trial(board, player):
    """
    Function takes a current board and the next player to move.
    The function plays a complete game starting with the input player.
    """
    current_player = player
    
    while (board.check_win() == None):
        free_space = board.get_empty_squares()
        plyr_nxt_sqr = free_space.pop(random.randrange(len(free_space))) 
        board.move(plyr_nxt_sqr[0], plyr_nxt_sqr[1], current_player)
        current_player = provided.switch_player(current_player)

def mc_update_scores(scores, board, player):
    """
    Function takes a grid of scores, a board from a
    completed game, and which player the machine player is.
    The function scores the completed board and updates the
    scores grid. Function does not return anything.
    """
    board_winner = board.check_win()
    other_player = provided.switch_player(player)
    if board_winner != provided.DRAW:
        for x_pos in range(board.get_dim()):
            for y_pos in range(board.get_dim()):
                cur_square = board.square(x_pos, y_pos)
                if (board_winner == player):
                    if (cur_square == player):
                        scores[x_pos][y_pos] += SCORE_CURRENT
                    elif (cur_square == other_player):  
                        scores[x_pos][y_pos] -= SCORE_OTHER
                elif (board_winner == other_player):
                    if (cur_square == player):
                        scores[x_pos][y_pos] -= SCORE_CURRENT
                    elif (cur_square == other_player):
                        scores[x_pos][y_pos] += SCORE_OTHER


def get_best_move(board, scores):  
    """
    Function takes a current board and a grid of scores. 
    The function should find all of the empty squares with
    the maximum score and randomly return one of them as a
    (row, column) tuple.
    """
    empty_squares = board.get_empty_squares()
    if (len(empty_squares) == 0):
        print "There are no moves left in the game."
        return 
    empty_scores = [scores[ind[0]][ind[1]] for ind in empty_squares]
    max_value = max(empty_scores)
    best_moves = [ind for ind in empty_squares if scores[ind[0]][ind[1]] == max_value]

    return best_moves[random.randrange(len(best_moves))]


def mc_move(board, player, trials):
    """
    Function takes a current board, which player the
    machine player is,and the number of trials to run.
    Returns square with optimum chance of winning.
    """

    score_grid = [[0 for dummy_x in range(board.get_dim())]
                   for dummy_y in range(board.get_dim())]
    for dummy in range(trials):
        test_board = board.clone()
        mc_trial(test_board, player)
        mc_update_scores(score_grid, test_board, player)
    return get_best_move(board, score_grid)
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
