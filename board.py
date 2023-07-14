from player import otamesiplayer
# from view import otamesiview

class otamesiboard:
    def __init__(self, r, masu):
        self.r = r
        self.turn = "A"

        # self.masu = [
        #         ["sg", "sl", "se"],
        #         ["", "sc", ""],
        #         ["", "gc", ""],
        #         ["ge", "gl", "gg"]
        #         ]
        # self.unserialize_masu = masu
        self.masu = masu
        # print(self.masu[0][0].name)

        self.Amasu = []
        self.Bmasu = []

    def is_my_piece(self, pie):
        if pie.player == self.whichturn():
            return True
        else:
            return False
        # ppx, ppy = piece_place
        # if self.masu[ppx][ppy].player == self.whichturn():
        #     return True
        # else:
        #     return False

    def change_turn(self):
        if self.turn == self.r.turn[0]:
            self.turn = self.r.turn[1]
        elif self.turn == self.r.turn[1]:
            self.turn = self.r.turn[0]

    def whichturn(self):
        # # return self.turn[1]
        # return "A"
        return self.turn

    # def on_click_move_button(self, a):
    #     p = otamesiplayer()
    #     if not self.choose_piece and not self.choose_place: # 既にコマを選択しているか
    #         if len(a) == 1: # 移動したい駒が持ち駒かどうか
    #             wt = self.whichturn()
    #             if wt == "A":
    #                 if self.Amasu[a[0]] == "": # 移動したいコマではなく、空を押してないか
    #                     print("コマを押してください")
    #                     return
    #                 else:
    #                     if self.Amasu[a[0]] in p.Atemoti:
    #                         self.choose_piece = [a[0]]
    #                         print(self.choose_piece)
    #                         return
    #                     else:
    #                         print("あなたのコマではありません")
    #                         return
    #             elif wt == "B":
    #                 if self.Bmasu[a[0]] == "": # 移動したいコマではなく、空を押してないか
    #                     print("コマを押してください")
    #                     return
    #                 else:
    #                     if self.Bmasu[a[0]] in p.Btemoti:
    #                         self.choose_piece = [a[0]]
    #                         print(self.choose_piece)
    #                         return
    #                     else:
    #                         print("あなたのコマではありません")
    #                         return
    #         else:
    #             wt = self.whichturn()
    #             if wt == "A":
    #                 if self.masu[a[0]][a[1]] == "": # 移動したいコマではなく、空を押してないか
    #                     print("コマを押してください")
    #                     return
    #                 else:
    #                     if self.masu[a[0]][a[1]] in p.Atemoti:
    #                         self.choose_piece = [a[0], a[1]]
    #                         print(self.choose_piece)
    #                         return
    #                     else:
    #                         print("あなたのコマではありません")
    #                         return
    #             elif wt == "B":
    #                 if self.masu[a[0]][a[1]] == "": # 移動したいコマではなく、空を押してないか
    #                     print("コマを押してください")
    #                     return
    #                 else:
    #                     if self.masu[a[0]][a[1]] in p.Btemoti:
    #                         self.choose_piece = [a[0], a[1]]
    #                         print(self.choose_piece)
    #                         return
    #                     else:
    #                         print("あなたのコマではありません")
    #                         return
    #     else:
    #         if len(a) == 2: # 選択した移動さきが盤面かどうか
    #             if len(self.choose_piece) == 2: # 選択してたコマが盤かどうか
    #                 self.choose_place = [a[0], a[1]]
    #                 if self.choose_piece == self.choose_place: # 選択してたコマに移動しようとしているか
    #                     self.choose_place = None
    #                     self.choose_piece = None
    #                     print("コマの選択を解除しました")
    #                     return
    #                 elif self.masu[a[0]][a[1]] != "": # 選択した移動さきにコマがあるか
    #                     wt = self.whichturn()
    #                     if wt == "A":
    #                         if self.masu[a[0]][a[1]] in p.Atemoti:
    #                             self.choose_piece = None
    #                             self.choose_place = None
    #                             print("自分のコマは取れません&選択解除")
    #                             return
    #                         piece_x, piece_y = self.choose_piece
    #                         place_x, place_y = self.choose_place
    #                         piece = self.masu[piece_x][piece_y]
    #                         torare = self.masu[place_x][place_y]
    #                         print(torare)
    #                         self.Amasu.append(torare)
    #                         p.Atemoti.append(torare)
    #                         p.Btemoti.remove(torare)
    #                         # 駒の移動
    #                         self.masu[place_x][place_y] = piece
    #                         self.masu[piece_x][piece_y] = ""
    #                     elif wt == "B":
    #                         if self.masu[a[0]][a[1]] in p.Btemoti:
    #                             self.choose_piece = None
    #                             self.choose_place = None
    #                             print("自分のコマは取れません&選択解除")
    #                             return
    #                         piece_x, piece_y = self.choose_piece
    #                         place_x, place_y = self.choose_place
    #                         torare = self.masu[place_x][place_y]
    #                         self.Bmasu.append(torare)
    #                         p.Btemoti.append(torare)
    #                         p.Atemoti.remove(torare)
    #                         # 駒の移動
    #                         self.masu[place_x][place_y] = piece
    #                         self.masu[piece_x][piece_y] = ""
    #                 else:
    #                     print(self.choose_place)
    #                     piece_x, piece_y = self.choose_piece
    #                     place_x, place_y = self.choose_place
    #                     piece = self.masu[piece_x][piece_y]
    #                     # 駒の移動
    #                     self.masu[place_x][place_y] = piece
    #                     self.masu[piece_x][piece_y] = ""
    #             else:
    #                 self.choose_place = [a[0], a[1]]
    #                 if self.masu[a[0]][a[1]] != "": # 選択した移動さきにコマがあるか
    #                     print("手持ちからは、空にしか置けません&選択解除")
    #                     self.choose_place = None
    #                     self.choose_piece = None
    #                     return
    #                 else:
    #                     print(self.choose_place)
    #                     place_x, place_y = self.choose_place
    #                     wt = self.whichturn()
    #                     if wt == "A":
    #                         piece = self.Amasu[self.choose_piece[0]]
    #                         # 駒の移動
    #                         self.masu[place_x][place_y] = piece
    #                         self.Amasu[self.choose_piece[0]] = ""
    #                         # b.Amasu.remove(piece)
    #                     elif wt == "B":
    #                         piece = self.Bmasu[self.choose_piece[0]]
    #                         # 駒の移動
    #                         self.masu[place_x][place_y] = piece
    #                         self.Bmasu[self.choose_piece[0]] = ""
    #                         # b.Bmasu.remove(piece)
    #         else:
    #             print("手持ちは移動さきに選択できません")
    #             print("＆選択解除しました")
    #             self.choose_piece = None
    #             return

    #     # 盤の表示を更新
    #     v = otamesiview()
    #     v.draw()

    #     # 駒の移動後の処理
    #     self.choose_piece = None
    #     self.choose_place = None
