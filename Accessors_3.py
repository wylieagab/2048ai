def terminalState(grid):
        return not grid.canMove()

def emptyTiles(grid):
    if terminalState(grid):
            return float("-inf")
    else:
        tiles = len(grid.getAvailableCells())
        return tiles

def highestValueTile(grid):
    if terminalState(grid):
        return float("-inf")
    maxTile = grid.getMaxTile()
    if maxTile == 1024 or maxTile == 2048 or maxTile == 4096 or maxTile == 8192:
        return maxTile
    else: return 0

def score(grid):
    score = 0
    for i in range(3):
        for j in range(3):
            score += grid.map[i][j]
    return score

def smoothness(grid):

        smoothness = 0

        for i in range(grid.size):
            for j in range(grid.size):
                if grid.crossBound((i, j+1)):
                    smoothness += abs(grid.map[i][j] - grid.map[i][j+1])
                if grid.crossBound((i, j-1)):
                    smoothness += abs(grid.map[i][j] - grid.map[i][j-1])
                if grid.crossBound((i+1, j)):
                    smoothness += abs(grid.map[i][j] - grid.map[i+1][j])
                if grid.crossBound((i-1, j)):
                    smoothness += abs(grid.map[i][j] - grid.map[i-1][j])
        return -smoothness

def Eval(grid, probability):
    empty = 100
    maxTile = grid.getMaxTile()
    if maxTile == 1024:
        empty = 200
    elif  maxTile == 2048:
        empty = 300
    return 10 * probability + emptyTiles(grid) * empty + smoothness(grid) + highestValueTile(grid)

