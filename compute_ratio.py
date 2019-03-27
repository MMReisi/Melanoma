import numpy as np


class Computer:
    def __init__(self, p, s):
        self.s = s
        self.p = p
        self.r = int()

    def find_r(self):
        self.r = (self.s / np.pi)**(1/2)
        return self

    def run(self):
        self.find_r()
        return self.p / (self.r * 2 * np.pi)
