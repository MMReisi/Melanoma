import numpy as np
import matplotlib.pyplot as plt


class Smooth:
    def __init__(self, image, label, n=3):
        self.img = image
        self.label = label
        self.h, self.w = self.img.shape
        self.min_y, self.min_x = 0, 0
        self.max_y, self.max_x = self.h, self.w
        self.n = n
        self.coordinates = []

    def find_coordinates(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.img[i, j] == self.label:
                    self.coordinates.append([i, j])

    def crop(self):
        x, y = zip(*self.coordinates)
        self.max_x = max(x)+1
        self.min_x = min(x)-1
        self.max_y = max(y)+1
        self.min_y = min(y)-1

    def smooth(self):
        timer = 0
        for j in range(self.min_y, self.max_y):
            if timer % 20 == 0:
                print('#', end='', flush=True)
            timer += 1
            for i in range(self.min_x, self.max_x):
                if self.img[i][j] != self.label:
                    temp = 0
                    for i_2 in range(-self.n, self.n):
                        try:
                            if self.img[i+i_2][j] == self.label:
                                temp += 1
                        except IndexError:
                            pass

                    for j_2 in range(-self.n, self.n):
                        try:
                            if self.img[i][j+j_2] == self.label:
                                temp += 1
                        except IndexError:
                            pass
                    if temp > int((8/10) * self.n * 4):
                        self.img[i][j] = self.label

    def run(self):
        self.find_coordinates()
        self.crop()
        self.smooth()
        return self.img

    def show_image(self):
        plt.imshow(self.img)
        plt.show()


if __name__ == '__main__':
    image_2 = [[0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 2, 2, 2, 0, 0, 0],
               [0, 0, 2, 0, 2, 0, 0, 0],
               [1, 0, 2, 2, 2, 0, 0, 0],
               [0, 0, 0, 1, 2, 0, 0, 1],
               [0, 0, 0, 1, 0, 0, 2, 0]]

    image_2 = np.array(image_2)
    S = Smooth(image_2, 2, n=2)
    S.run()
    S.show_image()
