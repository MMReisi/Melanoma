import numpy as np


class PS2:
    def __init__(self, p, s):
        self.s = s
        self.p = p
        self.r = int()

    def find_r(self):
        self.r = (self.s / np.pi)**(1/2)

    def run(self):
        self.find_r()
        return self.p / (self.r * 2 * np.pi)
