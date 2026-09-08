class Player:
    def __init__(self):
        # Người chơi bắt đầu là X
        self.current_symbol = "X"

    def switch_player(self):
        # Đổi lượt giữa X và O
        if self.current_symbol == "X":
            self.current_symbol = "O"
        else:
            self.current_symbol = "X"
