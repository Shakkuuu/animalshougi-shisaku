from piece import otamesipiece

class Giraffe(otamesipiece):
    move_range = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# before = [2, 2]
# after = [3, 2]

# g = Giraffe("gg", before, "A")
# g.can_move(after)
