import tkinter as tk

def show_message(canvas, text, size=600):
    """Hiển thị thông báo giữa màn hình"""
    canvas.create_text(size//2, size//2, text=text, font=("Arial", 24), fill="blue")

def reset_board(board, canvas, rows, cols, cell_size):
    """Xóa bàn cờ và vẽ lại"""
    canvas.delete("all")
    board.grid = [["" for _ in range(cols)] for _ in range(rows)]
    board.draw_board()
