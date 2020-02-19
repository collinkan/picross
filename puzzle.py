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
        
    def select(self, x: int, y: int) -> None:
        print("Testicles")
        if self.get_grid()[x][y] == 0: self.grid[x][y] = 1
        elif self.get_grid()[x][y] == 1: self.grid[x][y] = 0

    def mark(self, x: int, y:int) -> None:
        if self.get_grid()[x][y] == 0: self.grid[x][y] = 2
        elif self.get_grid()[x][y] == 2: self.grid[x][y] = 0

    def solved(self) -> bool:
        for i in range(len(self.get_grid())):
            for j in range(len(self.get_grid()[i])):
                if self.get_grid()[i][j] != self.get_solution()[i][j]:
                    return False
        return True

