import numpy as np
import matplotlib.pyplot as plt


class FilterPerimeter:
    def __init__(self, perimeter, image=None):
        self.img = image
        self.p = perimeter
        self.sort = []

    def filter(self):
        p = list(self.p)
        now = p.pop()
        self.sort = [now]
        x = []
        while p:
            d = []
            for i in p:
                d.append(((i[0] - now[0]) ** 2 + (i[1] - now[1]) ** 2) ** 0.5)
            dis = min(d)
            if dis > 3:
                if len(self.sort) == 0:
                    break
                now = self.sort.pop()
                x.append(now)
                continue
            place = d.index(dis)
            self.sort.append(p[place])
            d.pop(place)
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
