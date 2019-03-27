import numpy as np
import matplotlib.pyplot as plt


class Perimeter:
    def __init__(self, img, label, dots):
        self.img = img
        self.label = label
        self.dots = dots
        self.w, self.h = self.img.shape
        self.w -= 1
        self.h -= 1
        self.p = []

    def run(self):
        self.find_p()
        self.p = np.array(self.p)
        return self.p

    def find_p(self):
        for i in self.dots:
            x, y = i
            if (x == 0) | (y == 0) | (x == self.w) | (y == self.h):
                self.p.append([x, y])
                continue

            if self.img[x-1][y] != self.label:
                self.p.append([x, y])
                continue

            if self.img[x][y-1] != self.label:
                self.p.append([x, y])
                continue

            if self.img[x][y+1] != self.label:
                self.p.append([x, y])
                continue

            if self.img[x+1][y] != self.label:
                self.p.append([x, y])
                continue
        return self

    def show_image(self):
        plt.imshow(self.img)
        plt.scatter(self.p[:, 1], self.p[:, 0], s=5, c='red')
        plt.show()
        return self
