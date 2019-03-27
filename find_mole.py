import numpy as np
import matplotlib.pyplot as plt


class FindMole:
    def __init__(self, image, median, label):
        self.median = list(median)
        self.img = image
        self.label = label
        self.h, self.w = self.img.shape
        self.mole = [self.median]

    def find_mole(self):
        black = [self.median]
        dot = [self.median]
        timer = 0
        while dot:
            if timer % 2000 == 0:
                print('#', end='', flush=True)
            timer += 1
            x, y = dot.pop()
            for i in range(-1, 2):
                for j in range(-1, 2):
                    p = [x+i, y+j]
                    if p not in black:
                        try:
                            if self.img[p[0], p[1]] == self.label:
                                if p not in dot:
                                    dot.append(p)
                                if p not in self.mole:
                                    self.mole.append(p)
                        except IndexError:
                            pass
                        black.append(p)
        return self

    def run(self):
        self.find_mole()
        self.mole = np.array(self.mole)
        return self.mole

    def show_image(self, image=0):
        if type(image) == type(int):
            image = self.img

        plt.imshow(image)
        plt.scatter(self.mole[:, 1], self.mole[:, 0], c='red')
        plt.show()
        return self


if __name__ == '__main__':
    image_2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    image_2 = np.array(image_2)
    Mole = FindMole(image_2, [6, 9], 2)
    Mole.run()
    Mole.show_image()
