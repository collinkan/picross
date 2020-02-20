#Collin Kan

import PuzzleCreator as pc

class Puzzle:

    def __init__(self, imgname: str):
        self.imgname = imgname
        self.solution = pc.solution_maker(self.imgname)
        self.grid = [[0 for n in self.solution[0]] for r in self.solution]
        self.row_hints = pc.row_hints_maker(self.solution)
        self.col_hints = pc.col_hints_maker(self.solution)

    def get_grid(self) -> list:
        return self.grid

    def get_solution(self) -> list:
        return self.solution

    def get_row_hints(self) -> list:
        return self.row_hints

    def get_col_hints(self) -> list:
        return self.col_hints
        
    def select(self, x: int, y: int) -> None:
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

