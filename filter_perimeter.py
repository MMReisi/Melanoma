import numpy as np
import matplotlib.pyplot as plt


class FilterPerimeter:
    def __init__(self, perimeter, image=None):
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
            if dis > 3:
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

    def show_image(self):
        plt.imshow(self.img)
        plt.scatter(self.sort[:, 1], self.sort[:, 0], c='red', s=4)
        plt.show()

    def run(self):
        self.filter()
        return self.sort
