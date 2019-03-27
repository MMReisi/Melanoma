import matplotlib.image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import work_files


class Clustering:
    """ This class is used to cluster the pixels of the image according to their color"""
    def __init__(self, image, n_clusters=3):
        self.img = image
        self.n = n_clusters
        self.h, self.w, _ = self.img.shape
        self.output_img = np.array([])
        self.label = []

    def change_shape(self):
        self.img = self.img.reshape(self.w*self.h, 3)
        return self

    def make_cluster(self):
        cls = KMeans(n_clusters=self.n)
        cls.fit(self.img)
        self.output_img = cls.labels_.reshape(self.h, self.w)
        colors = cls.cluster_centers_.astype('uint8')**2
        mean = list(colors.mean(1))
        darkest = min(mean)
        self.label = mean.index(darkest)
        return self

    def run(self):
        self.change_shape()
        self.make_cluster()
        return self.output_img, self.label

    def show_image(self):
        plt.imshow(self.output_img)
        plt.show()
        return self


if __name__ == '__main__':
    img = work_files.OS()
    img = matplotlib.image.imread([i for i in img.run()][0])
    clr = Clustering(img)
    new_image, darkest_color_label = clr.run()
    clr.show_image()
