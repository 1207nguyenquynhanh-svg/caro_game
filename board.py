class Board:
    def __init__(self, canvas, rows, cols, cell_size):
        self.canvas = canvas
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [["" for _ in range(cols)] for _ in range(rows)]
        self.draw_board()

    def draw_board(self):
        size = self.rows * self.cell_size
        for i in range(self.rows + 1):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, size, fill="black")

        for i in range(self.cols + 1):
            y = i * self.cell_size
            self.canvas.create_line(0, y, size, y, fill="black")

    def place_mark(self, row, col, symbol):
        if self.grid[row][col] == "":
            x = col * self.cell_size + self.cell_size // 2
            y = row * self.cell_size + self.cell_size // 2
            self.canvas.create_text(x, y, text=symbol, font=("Arial", 16))
            self.grid[row][col] = symbol
            return True
        return False
