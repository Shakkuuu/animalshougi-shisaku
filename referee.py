class Referee():
    turn = ["A", "B"]
    # def __init__(self) -> None:
    #     self.turn = "A"

    def lion_count(self, square):
        count = 0
        for n in square:
            for m in n:
                if m.name in ["gl", "sl"]:
                    count += 1

        if count < 2:
            print("ライオンいないよー")
            return True
        else:
            return False

    # def change_turn(self):
    #     if self.turn == "A":
    #         self.turn == "B"
    #     elif self.turn == "B":
    #         self.turn == "A"
