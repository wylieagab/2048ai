from Accessors_3 import *
import time


def Decision(grid):
        
        limit = 8
        startTime = time.clock()
        
        return Minimize(grid[1], limit, startTime, float("-inf"), float("inf"), 1)
    
def Maximize(grid, depth, startTime, alpha, beta, probability):
        if terminalState(grid) or depth == 0 or (time.clock() - startTime) > 0.05:
            return Eval(grid, probability)
        
        maxUtility = float("-inf")
        
        for move in grid.getAvailableMoves():
            utility = Minimize(move[1], depth-1, startTime, alpha, beta, probability)
            
            if utility > maxUtility:
                maxUtility = utility
            
            if maxUtility >= beta:
                break
 
            if maxUtility > alpha: 
                alpha = maxUtility
            
        return maxUtility
    
def Minimize(grid, depth, startTime, alpha, beta, probability):
        if terminalState(grid) or depth == 0 or (time.clock() - startTime) > 0.05:
            return Eval(grid, probability)
        
        minUtility = float("inf")
        
        newTiles = grid.getAvailableCells()
        
        moves = []
        
        for move in newTiles:
            place2 = grid.clone()
            place4 = grid.clone()
            place2.insertTile(move, 2)
            place4.insertTile(move, 4)
            moves.append((place2, .90))
            moves.append((place4, .10))
        
        for move in moves:
            utility = Maximize(move[0], depth-1, startTime, alpha, beta, move[1])
            
            if utility < minUtility:
                minUtility = utility
            
            if minUtility <= alpha:
                break
            
            if minUtility < beta:
                beta = minUtility
            
        return minUtility