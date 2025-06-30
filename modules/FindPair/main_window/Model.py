from math import ceil

from PySide6 import QtCore
from PySide6.QtCore import Slot, QObject
from random import shuffle


def grid_btn(buttons: list[int]):
    N = len(buttons)
    r, c = 0, 0
    for cols in range(1, N + 1):
        rows = ceil(N / cols)
        if rows <= cols:
            r = rows
            c = cols
            break
    grid = []
    for i in range(r):
        row = []
        for j in range(c):
            idx = i * c + j
            if idx < N:
                row.append(buttons[idx])
        grid.append(row)
    return grid


class FindPairModel(QObject):
    def __init__(self, context, /):
        super().__init__()
        self.context = context
        self.guesses = 0
        self.pair_count = 5
        self.preview_time = 3000
        self.Endless = False
        self.cards = []
        self.found_pairs = 0
        self.hide_timer = QtCore.QTimer()
        self.hide_timer.setInterval(self.preview_time)

    @Slot()
    def start(self):
        self.create_cards()

    def create_cards(self):
        self.cards = [i // 2 + 1 for i in range(self.pair_count * 2)]
        print(self.cards)
        shuffle(self.cards)
        self.cards = grid_btn(self.cards)
        print(self.cards)

    def get_cards(self):
        return self.cards
