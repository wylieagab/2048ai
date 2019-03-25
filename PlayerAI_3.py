import random
from BaseAI_3 import BaseAI
from Accessors_3 import *
from ExpectMiniMax_3 import *
from Grid_3 import *

class PlayerAI(BaseAI):
        
    def getMove(self, grid):
    	# Runs expectimax with hueristic wieght to choose a move
        moves = grid.getAvailableMoves()
        maxUtility = float("-inf")
        nextMove = -1
        
        for move in moves:
            utility = Decision(move)

            if utility >= maxUtility:
                maxUtility = utility
                nextMove = move
                
        return nextMove[0]
    
