class otamesipiece():
    def __init__(self, name: str, place: list, player: str):
        self.name = name
        self.place = place
        self.player = player

    def can_move(self, after):

        gmove = [x - y for (x, y) in zip(after, self.place)]

        if self.name in ["gC", "sC", "gc", "sc"]:
            if self.is_promoted == True:
                self.move_range = self.chicken_move_range

        if self.player == "B":
            B_move_range = []
            Bmr = []
            for n in self.move_range:
                for m in n:
                    Bmr.append(m*-1)
                B_move_range.append(Bmr)
                Bmr = []
            if gmove in B_move_range:
                print("Ok")
                return True
            else:
                print("noooo")
                return False
        else:
            if gmove in self.move_range:
                print("Ok")
                return True
            else:
                print("noooo")
                return False

    def move_position(self, after):
        self.place = after
        print(f'move_position後の座標{self.place}')

    def change_my_player(self, pl):
        self.player= pl
        print(f'change_my_player後のplayer{self.player}')
