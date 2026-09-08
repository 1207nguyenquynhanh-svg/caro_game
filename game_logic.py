def check_winner(grid, row, col, symbol):
    """
    Kiểm tra xem người chơi vừa đánh tại (row, col) có thắng không.
    Điều kiện thắng: 5 quân liên tiếp theo hàng, cột hoặc chéo.
    """
    directions = [
        (1, 0),   # dọc
        (0, 1),   # ngang
        (1, 1),   # chéo xuống phải
        (1, -1)   # chéo xuống trái
    ]

    for dr, dc in directions:
        count = 1

        # Kiểm tra xuôi
        r, c = row + dr, col + dc
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == symbol:
            count += 1
            r += dr
            c += dc

        # Kiểm tra ngược
        r, c = row - dr, col - dc
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == symbol:
            count += 1
            r -= dr
            c -= dc

        if count >= 5:
            return True

    return False
