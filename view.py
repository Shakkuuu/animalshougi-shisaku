import tkinter as tk

piece_ = ["sc", "sl", "se", "sl", "gc", "gl", "ge", "gg"]

class otamesiview:
    BOARDHEIGHT = 4
    BOARDWIDTH = 3
    cell = None
    turn_view = None
    mess = None
    surrender = None
    message = ""

    choose_place = None
    choose_piece = None

    def __init__(self, r, b, p, emp):
        self.r = r
        self.b = b
        self.p = p
        self.emp = emp
        # Tkinterウィンドウ
        self.root = tk.Tk()
        self.root.title("どうぶつしょうぎ")
        self.draw()
        self.root.mainloop()

    def draw(self):
        print(f'今の盤面:{self.b.masu}')
        for i in range(self.BOARDHEIGHT):
            for j in range(self.BOARDWIDTH):
                self.cell = tk.Button(self.root, width=10, height=5)
                self.cell.grid(row=i+1, column=j)
                piece = self.b.masu[i][j]
                self.cell.config(text=piece.player+piece.name, fg="black", command=lambda x=i, y=j, pie = piece: self.on_click_move_button([x, y], pie))
                self.cell.bind("<ButtonPress>", self.change_color)
        print(f'今のAの手持ちコマ:{self.b.Amasu}')
        for k in range(8):
            self.cell = tk.Button(self.root, width=5, height=5)
            self.cell.grid(row=5, column=k)
            self.cell.config(text="")
        for k in range(len(self.b.Amasu)):
            self.cell = tk.Button(self.root, width=5, height=5)
            self.cell.grid(row=5, column=k)
            piece = self.b.Amasu[k]
            self.cell.config(text=piece.player+piece.name, fg="black", command=lambda y=k, pie=piece: self.on_click_move_button([y], pie))
            self.cell.bind("<ButtonPress>", self.change_color)
        print(f'今のBの手持ちコマ:{self.b.Bmasu}')
        for l in range(8):
            self.cell = tk.Button(self.root, width=5, height=5)
            self.cell.grid(row=0, column=l)
            self.cell.config(text="")
        for l in range(len(self.b.Bmasu)):
            self.cell = tk.Button(self.root, width=5, height=5)
            self.cell.grid(row=0, column=l)
            piece = self.b.Bmasu[l]
            self.cell.config(text=piece.player+piece.name, fg="black", command=lambda y=l, pie=piece: self.on_click_move_button([y], pie))
            self.cell.bind("<ButtonPress>", self.change_color)

        print(f'今のAの所有:{self.p.Atemoti}')
        print(f'今のBの所有:{self.p.Btemoti}')

        self.turn_view = tk.Label(self.root)
        self.turn_view.grid(row=2, column=4)
        whichturn = self.b.whichturn()
        self.turn_view.config(text="今は" + whichturn + "のターンです")

        self.mess = tk.Label(self.root)
        self.mess.grid(row=3, column=4)
        self.mess.config(text="　　　　　"+self.message+"　　　　　", background='white')

        self.surrender = tk.Button(self.root, text="ゲームを終了する", command=self.root.destroy)
        self.surrender.grid(row=4, column=4)

    def on_click_move_button(self, a, pie):
        print(pie)
        if not self.choose_piece and not self.choose_place: # 既にコマを選択しているか
            if len(a) == 1: # 移動したい駒が持ち駒かどうか
                if pie.name == "": # 選択した移動したいこまが空白かどうか
                    print("コマを押してください")
                    return
                else:
                    print(f'手持ちから出すときのやつ：{pie.player}')
                    if self.b.is_my_piece(pie) == True: # 自分のコマかどうか
                        self.choose_piece = [a[0]]
                        print(f'選択したコマの座標{self.choose_piece}')
                        return
                    else:
                        print("あなたのコマではありません")
                        self.message = "あなたのコマではありません"
                        print()
                        self.draw()
                        return
            else:
                if pie.name == "": # 選択した移動したいこまが空白かどうか
                    print("コマを押してください")
                    return
                else:
                    if self.b.is_my_piece(pie) == True: # 自分のコマかどうか
                        self.choose_piece = [a[0], a[1]]
                        print(f'選択したコマの座標{self.choose_piece}')
                        return
                    else:
                        print("あなたのコマではありません")
                        self.message = "あなたのコマではありません"
                        print()
                        self.draw()
                        return
        else:
            if len(a) == 2: # 選択した移動さきが盤面かどうか
                if len(self.choose_piece) == 2: # 選択してたコマが盤かどうか
                    if self.b.masu[self.choose_piece[0]][self.choose_piece[1]].can_move(a):
                        pass
                    else:
                        print("コマの移動範囲外です。")
                        self.choose_place = None
                        self.choose_piece = None
                        print("コマの選択を解除しました")
                        print()
                        self.message = "コマの移動範囲外です。コマの選択を解除しました"
                        self.draw()
                        return

                    if self.choose_piece == a: # 選択してたコマに移動しようとしているか
                        self.choose_place = None
                        self.choose_piece = None
                        print("コマの選択を解除しました")
                        print()
                        self.message = "コマの選択を解除しました"
                        self.draw()
                        return
                    elif pie.name != "": # 選択した移動さきにコマがあるか
                        if self.b.is_my_piece(pie) == True:
                            self.choose_piece = None
                            self.choose_place = None
                            print("自分のコマは取れません&選択解除")
                            print()
                            self.message = "自分のコマは取れません&選択解除"
                            self.draw()
                            return
                        self.choose_place = [a[0], a[1]]
                        print(f'選択した移動さき:{self.choose_place}')
                        piece_x, piece_y = self.choose_piece
                        place_x, place_y = self.choose_place
                        piece = self.b.masu[piece_x][piece_y]
                        torare = self.b.masu[place_x][place_y]
                        print(f'取られたコマ:{torare}')
                        if torare.name in ["gC", "sC"]: # 取られたコマが鶏だったらdepromoteする
                            torare.depromotion()
                        if piece.name in ["gc", "sc"]: # 移動するコマがひよこだったら
                            if piece.player == "A":
                                if place_x == 0: # 一番奥まで行ってたら
                                    piece.promotion()
                            elif piece.player == "B":
                                if place_x == 3: # 一番奥まで行ってたら
                                    piece.promotion()
                        if self.b.masu[self.choose_piece[0]][self.choose_piece[1]].player == "A":
                            print("Aの取る場面")
                            torare.change_my_player(piece.player)
                            self.b.Amasu.append(torare)
                            self.p.Atemoti.append(torare)
                            self.p.Btemoti.remove(torare)
                            print(f'torare後のplayer: {torare.name}:{torare.player}')
                            # 駒の移動
                            piece.move_position([place_x, place_y])
                            self.b.masu[place_x][place_y] = piece
                            self.b.masu[piece_x][piece_y] = self.emp
                            print(f'移動後の座標: {piece.name}:{piece.place}')
                        elif self.b.masu[self.choose_piece[0]][self.choose_piece[1]].player == "B":
                            print("Bの取る場面")
                            torare.change_my_player(piece.player)
                            self.b.Bmasu.append(torare)
                            self.p.Btemoti.append(torare)
                            self.p.Atemoti.remove(torare)
                            print(f'torare後のplayer: {torare.name}:{torare.player}')
                            # 駒の移動
                            piece.move_position([place_x, place_y])
                            self.b.masu[place_x][place_y] = piece
                            self.b.masu[piece_x][piece_y] = self.emp
                            print(f'移動後の座標: {piece.name}:{piece.place}')
                    else:
                        self.choose_place = [a[0], a[1]]
                        print(f'選択した移動さき:{self.choose_place}')
                        piece_x, piece_y = self.choose_piece
                        place_x, place_y = self.choose_place
                        piece = self.b.masu[piece_x][piece_y]
                        place = self.b.masu[place_x][place_y]
                        if piece.name in ["gc", "sc"]: # 移動するコマがひよこだったら
                            if piece.player == "A":
                                if place_x == 0: # 一番奥まで行ってたら
                                    piece.promotion()
                            elif piece.player == "B":
                                if place_x == 3: # 一番奥まで行ってたら
                                    piece.promotion()
                        # 駒の移動
                        piece.move_position(self.choose_place)
                        self.b.masu[place_x][place_y] = piece
                        self.b.masu[piece_x][piece_y] = place
                        print(f'移動後の座標: {piece.name}:{piece.place}')
                else:
                    if pie.name != "": # 選択した移動さきにコマがあるか
                        print("手持ちからは、空にしか置けません&選択解除")
                        self.choose_place = None
                        self.choose_piece = None
                        print()
                        self.message = "手持ちからは、空にしか置けません&選択解除"
                        self.draw()
                        return
                    else:
                        self.choose_place = [a[0], a[1]]
                        print(f'選択した移動さき:{self.choose_place}')
                        place_x, place_y = self.choose_place
                        if self.b.whichturn() == "A":
                            piece = self.b.Amasu[self.choose_piece[0]]
                            # 駒の移動
                            piece.move_position(self.choose_place)
                            self.b.masu[place_x][place_y] = piece
                            # b.Amasu[self.choose_piece[0]] = ""
                            self.b.Amasu.remove(piece)
                            print(f'移動後の座標: {piece.name}:{piece.place}')
                        elif self.b.whichturn() == "B":
                            piece = self.b.Bmasu[self.choose_piece[0]]
                            # 駒の移動
                            piece.move_position(self.choose_place)
                            self.b.masu[place_x][place_y] = piece
                            # b.Bmasu[self.choose_piece[0]] = ""
                            self.b.Bmasu.remove(piece)
                            print(f'移動後の座標: {piece.name}:{piece.place}')
            else:
                print("手持ちは移動さきに選択できません＆選択解除しました")
                self.choose_piece = None
                print()
                self.message = "手持ちは移動さきに選択できません＆選択解除しました"
                self.draw()
                return

        # 勝ち負け判定
        if self.r.lion_count(self.b.masu) == True:
            whichturn = self.b.whichturn()
            self.message = "ライオンをとったので" + whichturn + "の勝ちです!"
            print(f'self.message{self.message}')

        # 盤の表示を更新
        self.b.change_turn()
        print()
        print("ターン変更")
        print()
        print(f'現在のターン:{self.b.turn}')
        self.draw()

        # 駒の移動後の処理
        self.choose_piece = None
        self.choose_place = None


    def change_color(self, event):
        if event.widget["fg"] == "red":
            event.widget["fg"] = "black"
            return
        else:
            event.widget["fg"] = "red"

if __name__ == "__main__":
    # Tkinterウィンドウ
    root = tk.Tk()
    root.title("どうぶつしょうぎ")
    v = otamesiview()
    v.draw()

    root.mainloop()
