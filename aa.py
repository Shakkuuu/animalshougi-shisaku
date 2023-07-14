import tkinter as tk
from view import otamesiview
from referee import Referee
from board import otamesiboard
from player import otamesiplayer
from chick import Chick
from elephant import Elephant
from giraffe import Giraffe
from lion import Lion
from piece import otamesipiece


class Game:

    # self.masu = [
    #             ["sg", "sl", "se"],
    #             ["", "sc", ""],
    #             ["", "gc", ""],
    #             ["ge", "gl", "gg"]
    #             ]

    def __init__(self) -> None:
        self.r = Referee()

        self.sg = Giraffe("sg", [0, 0], "B")
        self.sl = Lion("sl", [0, 1], "B")
        self.se = Elephant("se", [0, 2], "B")
        self.sc = Chick("sc", [1, 1], "B", False)
        self.gc = Chick("gc", [2, 1], "A", False)
        self.ge = Elephant("ge", [3, 0], "A")
        self.gl = Lion("gl", [3, 1], "A")
        self.gg = Giraffe("gg", [3, 2], "A")
        self.emp = otamesipiece("", [], "")

        self.masu = [
            [self.sg, self.sl, self.se],
            [self.emp, self.sc, self.emp],
            [self.emp, self.gc, self.emp],
            [self.ge, self.gl, self.gg]
            ]

        self.Atemoti = [self.gc, self.ge, self.gl, self.gg]
        self.Btemoti = [self.sc, self.se, self.sl, self.sg]

        # print(self.masu[0][0].can_move([1, 0]))

        self.b = otamesiboard(self.r, self.masu)
        self.p = otamesiplayer(self.Atemoti, self.Btemoti)
        self.v = otamesiview(self.r, self.b, self.p, self.emp)

    # def display(self):
    #     v = otamesiview()
    #     v.vimain()

if __name__ == "__main__":
    game = Game()
    # game.display()
