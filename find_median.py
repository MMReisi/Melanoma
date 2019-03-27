import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt


class Median:
    def __init__(self, image, label):
        self.label = label
        self.img = image
        self.h, self.w = self.img.shape
        self.coordinates = []
        self.median = [0, 0]

    def find_coordinates(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.img[i, j] == self.label:
                    self.coordinates.append([i, j])
        print('#', end='', flush=True)
        return self

    def filter_and_find_median(self):
        self.coordinates = np.array(self.coordinates)
        len_before = len(self.coordinates)
        while True:
            mean = np.mean(self.coordinates, axis=0)
            distances = np.zeros(len_before)
            for i in range(len_before):
                distances[i] = euclidean(i, mean)
            self.coordinates = self.coordinates[distances <= (distances.mean()+distances.var())]
            if len(self.coordinates) == len_before:
                break
            len_before = len(self.coordinates)
        self.median = self.coordinates.mean(axis=0).astype(int)
        print('#', end='', flush=True)
        return self

    def run(self):
        self.find_coordinates()
        self.filter_and_find_median()
        return self.median

    def show_image(self):
        plt.imshow(self.img)
        plt.scatter(self.median[1], self.median[0], c='red', s=100)
        plt.show()
        return self


if __name__ == '__main__':
    image_2 = [[2, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 2, 2, 2, 0, 0, 0],
               [0, 0, 2, 2, 2, 0, 0, 0],
               [1, 0, 1, 1, 2, 0, 0, 0],
               [0, 0, 0, 1, 2, 0, 0, 1],
               [0, 0, 0, 1, 0, 0, 0, 0]]
    image_2 = np.array(image_2)
    M = Median(image_2, 2)
    median = M.run()
    M.show_image()
