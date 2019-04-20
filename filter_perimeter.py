import numpy as np
import matplotlib.pyplot as plt


class FilterPerimeter:
    def __init__(self, perimeter, image=None, min_distance=3):
        self.m_d = min_distance
        self.img = image
        self.p = perimeter
        self.sort = []

    @staticmethod
    def min_distance(points, root):
        d = []
        for i in points:
            d.append(((i[0] - root[0]) ** 2 + (i[1] - root[1]) ** 2) ** 0.5)
        return d, min(d)

    def filter(self):
        p = list(self.p)
        now = p.pop()
        self.sort = [now]
        x = []
        while p:
            d, dis = self.min_distance(p, now)
            if dis > self.m_d:
                if len(self.sort) == 0:
                    break
                now = self.sort.pop()
                x.append(now)
                continue
            place = d.index(dis)
            self.sort.append(p[place])
            now = p.pop(place)
        self.sort.reverse()
        self.sort = np.array(x)
        return self

    def show_image(self, image=0):
        if type(image) == type(int):
            image = self.img
        plt.imshow(image)
        plt.scatter(self.sort[:, 1], self.sort[:, 0], c='red', s=4)
        plt.show()
        return self

    def run(self):
        self.filter()
        return self.sort
