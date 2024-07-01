import tkinter as tk
from tkinter import messagebox


def solve_sudoku(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(puzzle, num, (row, col)):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0

    return False

def is_valid(puzzle, num, pos):
    
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j) 
    return None

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.puzzle = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

        self.create_puzzle()

    def create_puzzle(self):
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    entry = tk.Entry(self.root, width=5, font=('Arial', 18), justify='center')
                else:
                    entry = tk.Entry(self.root, width=5, font=('Arial', 18), justify='center', state='disabled')
                    entry.insert(0, str(self.puzzle[i][j]))
                entry.grid(row=i, column=j, padx=3, pady=3)
                row.append(entry)
            self.entries.append(row)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, columnspan=4, padx=10, pady=10)

        rules_button = tk.Button(self.root, text="Show Rules", command=self.show_rules)
        rules_button.grid(row=9, column=5, columnspan=4, padx=10, pady=10)

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].get() == "":
                    self.puzzle[i][j] = 0
                else:
                    self.puzzle[i][j] = int(self.entries[i][j].get())

        if solve_sudoku(self.puzzle):
            self.update_board()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists for the given puzzle.")

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.puzzle[i][j]))

    def show_rules(self):
        rules = (
            "1. Each row must contain the numbers from 1 to 9, without repetitions.\n"
            "2. Each column must contain the numbers from 1 to 9, without repetitions.\n"
            "3. The digits can only appear once in each 3x3 box.\n"
        )
        messagebox.showinfo("Sudoku Rules", rules)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = SudokuSolverGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
