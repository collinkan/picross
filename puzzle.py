#Collin Kan

class puzzle:

    def __init__(self, solution: list, row_hints: list, col_hints: list):
        self.grid = [[0 for n in solution[0]] for r in solution]
        self.solution = solution
        self.row_hints = row_hints
        self.col_hints = col_hints

    def add(self) -> None:
        return
    