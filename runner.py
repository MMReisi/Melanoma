import clustering
import find_median
import smoothing
import find_mole
import perimeter
import matplotlib.image
import compute_ratio
import filter_perimeter
import work_files
import matplotlib.pyplot as plt
import numpy as np


class Run:
    def __init__(self, image: np.ndarray, n_cluster=3, n_s=4, m_s=0.5):
        self.n_s = n_s
        self.m_s = m_s
        self.n_cluster = n_cluster
        self.image = image
        self.raw_image = image.copy()
        self.Clustering = clustering.Clustering
        self.Smooth = smoothing.Smooth
        self.Median = find_median.Median
        self.FindMole = find_mole.FindMole
        self.Compute = compute_ratio.Computer
        self.Perimeter = perimeter.Perimeter
        self.Filter = filter_perimeter.FilterPerimeter
        self.p = 0
        self.s = []
        self.label = 0
        self.median = [0, 0]
        self.mole = []
        self.ratio = 0
        self.perimeter = 0

    def run(self):
        self.Clustering = clustering.Clustering(self.image, n_clusters=self.n_cluster)
        print('<|', end='', flush=True)
        self.image, self.label = self.Clustering.run()
        print('|', end='', flush=True)
        self.Smooth = smoothing.Smooth(self.image.copy(), self.label, n=self.n_s, m=self.m_s)
        self.image = self.Smooth.run()
        print('|', end='', flush=True)
        self.Median = find_median.Median(self.image, self.label)
        self.median = self.Median.run()
        print('|', end='', flush=True)
        self.FindMole = find_mole.FindMole(self.image, self.median, self.label)
        self.mole = self.FindMole.run()
        print('|', end='', flush=True)
        self.Perimeter = perimeter.Perimeter(self.image, self.label, self.mole)
        self.p = self.Perimeter.run()
        print('|', end='', flush=True)
        self.Filter = filter_perimeter.FilterPerimeter(self.p, self.image)
        self.p = self.Filter.run()
        print('|', end='', flush=True)
        self.perimeter = len(self.p)
        self.s = len(self.mole)
        self.Compute = compute_ratio.Computer(self.perimeter, self.s)
        print('|', end='', flush=True)
        self.ratio = self.Compute.run()
        print('|>')
        return self

    def show_images(self):
        self.Clustering.show_image()
        self.Smooth.show_image()
        self.Median.show_image(self.raw_image)
        self.FindMole.show_image(self.raw_image)
        self.Perimeter.show_image(self.raw_image)
        self.Filter.show_image(self.raw_image)
        return self


if __name__ == '__main__':
    imgs = work_files.OS()
    imgs = [i for i in imgs.run()]
    img = input('Enter the name of picture \nfor example \'low_risk_2.jpg\' : ')
    if img not in imgs:
        print(' I can\'t find this image make sure about spelling')
        exit()
    img = matplotlib.image.imread(img)
    plt.imshow(img)
    plt.show()
    obj = Run(img)
    obj.run()
    obj.show_images()
    print('Area : ', obj.s)
    print('Perimeter : ', obj.perimeter)
    print('Ratio : ', obj.ratio)
