paperRolls = 0

with open('input.txt') as file:
    grid = [line.strip() for line in file.readlines()]
    collumns = len(grid[0])
    rows = len(grid)
    print(grid)
    while True:
        newGrid = [list(row) for row in grid]
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                
                if grid[i][j] == "@":
                    adjacentAmount = 0

                    for rOffset in [-1, 0, 1]:
                        for cOffset in [-1, 0, 1]:
                            if rOffset==0 and cOffset== 0:
                                continue
                
                            newRow, newCollum = i + rOffset, j + cOffset

                            if 0 <= newRow < rows and 0 <= newCollum < collumns:
                                if grid[newRow][newCollum] == "@":
                                    adjacentAmount += 1

                    if adjacentAmount < 4:
                        paperRolls += 1
                        newGrid[i][j] = "x"
                    else:
                        newGrid[i][j] = "@"
                        
                elif grid[i][j] == "x":
                    newGrid[i][j] = "x"
                elif grid[i][j] == ".":
                    newGrid[i][j] = "."
                        
                
        if grid == newGrid:
            break
        grid = newGrid
print(paperRolls)