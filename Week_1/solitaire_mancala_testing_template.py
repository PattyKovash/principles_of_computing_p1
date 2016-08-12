"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class()
    
#    
#    config1 = [0, 0, 1, 1, 3, 5, 0]    
#    game.set_board(config1)   
#    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
#    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
#    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
#    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")  
    
    # add tests using suite.run_test(....) here

    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([0]), "Test #0: init")
    
    # test get_num_seeds
    config1 = [0, 0, 1, 1, 3, 5, 0]  
    config2 = [0, 0, 0, 0, 0]
    config3 = [0,3,6,3]
    game.set_board(config1)
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1: get_num_seeds")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #2: get_num_seeds")
    game.apply_move(5)
    suite.run_test(str(game), str([0, 0, 4, 2, 2, 1, 1]), "Test #2: get_num_seeds")
    
    
    
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
 
    
    # report number of tests and failures
    suite.report_results()

