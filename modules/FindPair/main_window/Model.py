from math import ceil
from typing import Any

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
        self.pair_count = None
        self.preview_time = None
        self.Endless = None
        self.context = context
        self.guesses = 0
        self.load_settings()
        self.cards = []
        self.found_pairs = 0
        self.hide_timer = QtCore.QTimer()
        assert isinstance(self.preview_time, int)
        self.hide_timer.setInterval(self.preview_time)

    def load_settings(self):
        data = self.context.settingsManager.load(
            ['pair_count', 'preview_time', 'Endless'], [int, int, bool], 'FindPair')
        self.pair_count, self.preview_time, self.Endless = data['pair_count'], data['preview_time'], data['Endless']

    @Slot()
    def start(self):
        self.create_cards()

    def create_cards(self):
        print(f"before: {self.cards}")
        self.load_settings()
        self.cards = [i // 2 + 1 for i in range(self.pair_count * 2)]
        shuffle(self.cards)
        self.cards = grid_btn(self.cards)
        print(f"after: {self.cards}")

    def get_cards(self):
        return self.cards
