"""
Coursera
Rice University
Principles to Computing Part 1

A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game

Implementation by PK
August 2016
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    win_rate = 0.0
    best_move = 0 
    for init_move in range(1, MAX_REMOVE + 1):
        wins = 0
        for _ in range(TRIALS):
            counter = init_move
            comp_move = 1            
            while (counter < num_items):
                comp_move += 1
                counter += random.randrange(1, MAX_REMOVE + 1)               
            if (comp_move % 2 != 0):
                wins += 1           
        current_win_rate = float(wins) / TRIALS  
        if (win_rate < current_win_rate):
            win_rate = current_win_rate
            best_move = init_move            
    return best_move 

    
def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Current value is " + str(current_items) + ". Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)
        
    
                 
    