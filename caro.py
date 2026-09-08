import tkinter as tk
from board import Board
from player import Player
from game_logic import check_winner

# Cấu hình
size = 600
rows = 20
cols = 20
cell_size = size // rows

# Tạo cửa sổ
root = tk.Tk()
root.title("Cờ Caro")

canvas = tk.Canvas(root, width=size, height=size, bg="white")
canvas.pack()

# Khởi tạo bàn cờ và người chơi
board = Board(canvas, rows, cols, cell_size)
player = Player()

# Xử lý click chuột
def handle_click(event):
    row = event.y // cell_size
    col = event.x // cell_size

    if board.place_mark(row, col, player.current_symbol):
        if check_winner(board.grid, row, col, player.current_symbol):
            canvas.create_text(size//2, size//2, text=f"{player.current_symbol} thắng!", font=("Arial", 24), fill="red")
            canvas.unbind("<Button-1>")
        else:
            player.switch_player()

canvas.bind("<Button-1>", handle_click)

root.mainloop()
