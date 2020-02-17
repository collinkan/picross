#Collin Kan

class puzzle:

    def __init__(self, solution: list, row_hints: list, col_hints: list):
        self.grid = [[0 for n in solution[0]] for r in solution]
        self.solution = solution
        self.row_hints = row_hints
        self.col_hints = col_hints

    def get_grid(self) -> list:
        return self.grid

    def get_solution(self) -> list:
        return self.solution

    def get_row_hints(self) -> list:
        return self.row_hints

    def get_col_hints(self) -> list:
        return self.col_hints
        
    def cross(self, x: int, y: int) -> None:
        if self.get_grid()[x][y] == 0: self.grid[x][y] = 1
        if self.get_grid()[x][y] == 1: self.grid[x][y] = 0