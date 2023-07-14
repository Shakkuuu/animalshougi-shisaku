from piece import otamesipiece

class Chick(otamesipiece):
    move_range = [[-1, 0]]
    chicken_move_range = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1]]
    def __init__(self, name: str, place: list, player: str, is_promoted: bool):
        super().__init__(name, place, player) # 基底クラスのコンストラクタをオーバーライド
        self.is_promoted = is_promoted

    def promotion(self):
        self.is_promoted = True
        if self.name == "gc":
            self.name = "gC"
        elif self.name == "sc":
            self.name = "sC"

    def depromotion(self):
        self.is_promoted = False
        if self.name == "gC":
            self.name = "gc"
        elif self.name == "sC":
            self.name = "sc"
