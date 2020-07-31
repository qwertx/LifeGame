import random
from copy import deepcopy


class LifeGame():
    def __init__(self, width, height, init_amount, seed):
        self.width = width
        self.height = height
        self.total = self.width * self.height
        self.init_amount = init_amount
        self.board = [1] * init_amount + [0] * (self.width * self.height - init_amount)
        self.tmp_board = []
        self.gen_count = 0
        self.running = 1
        random.seed(seed)
        random.shuffle(self.board)

    def count_live(self, curr):
        upper_left = max(curr - self.width - 1, -1)
        upper = max(curr - self.width, -1)
        upper_right = max(curr - self.width + 1, -1)
        left = max(curr - 1, -1)
        right = min(curr + 1, self.total)
        lower_left = min(curr + self.width - 1, self.total)
        lower = min(curr + self.width, self.total)
        lower_right = min(curr + self.width + 1, self.total)
        surroundings = [upper_left, upper, upper_right, left, right, lower_left, lower, lower_right]

        live_count = 0
        for s in surroundings:
            if s != -1 and s != self.total and self.tmp_board[s] == 1:
                live_count += 1

        return live_count

    def generation(self):
        self.tmp_board = deepcopy(self.board)
        for i in range(self.total):
            live_count = self.count_live(i)
            if live_count == 2:
                pass
            elif live_count == 3:
                self.board[i] = 1
            else:
                self.board[i] = 0

    def loop(self):
        while self.running:
            self.generation()
            self.gen_count += 1
            



