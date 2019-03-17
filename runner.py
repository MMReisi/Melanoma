import clustering
import find_median
import smoothing
import find_mole
import perimeter
import matplotlib.image
import compute_ratio
import work_files
import matplotlib.pyplot as plt
import numpy as np


class Run:
    def __init__(self, image: np.ndarray, n_cluster=3, n_s=4, m_s=0.5):
        self.n_s = n_s
        self.m_s = m_s
        self.n_cluster = n_cluster
        self.image = image
        self.cls = clustering.Clustering
        self.S = smoothing.Smooth
        self.M = find_median.Median
        self.Mole = find_mole.FindMole
        self.c = compute_ratio.PS2
        self.ps = perimeter.Perimeter
        self.p = 0
        self.s = []
        self.label = 0
        self.median = [0, 0]
        self.mole = []
        self.ratio = 0
        self.perimeter = 0

    def run(self):
        self.cls = clustering.Clustering(self.image, n_clusters=self.n_cluster)
        print('<|', end='', flush=True)
        self.image, self.label = self.cls.run()
        print('|', end='', flush=True)
        self.S = smoothing.Smooth(self.image.copy(), self.label, n=self.n_s, m=self.m_s)
        self.image = self.S.run()
        print('|', end='', flush=True)
        self.M = find_median.Median(self.image, self.label)
        self.median = self.M.run()
        print('|', end='', flush=True)
        self.Mole = find_mole.FindMole(self.image, self.median, self.label)
        self.mole = self.Mole.run()
        print('|', end='', flush=True)
        self.ps = perimeter.Perimeter(self.image, self.label, self.mole)
        self.p = self.ps.run()
        self.perimeter = len(self.p)
        self.s = len(self.mole)
        self.c = compute_ratio.PS2(self.perimeter, self.s)
        print('|', end='', flush=True)
        self.ratio = self.c.run()
        print('|>')

    def show_images(self):
        self.cls.show_image()
        self.S.show_image()
        self.M.show_image()
        self.Mole.show_image()
        self.ps.show_image()


if __name__ == '__main__':
    img = work_files.OS()
    img = [i for i in img.run()][0]
    img = matplotlib.image.imread(img)
    plt.imshow(img)
    plt.show()
    obj = Run(img)
    obj.run()
    obj.show_images()
    print('Area : ', obj.s)
    print('Perimeter : ', obj.perimeter)
    print('Ratio : ', obj.ratio)
