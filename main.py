import clustering
import find_median
import smoothing
import find_mole
import p_s
import matplotlib.image
import compute_ratio
import work_files


class Run:
    def __init__(self, image):
        self.img = image
        self.cls = clustering.Clustering
        self.S = smoothing.Smooth
        self.M = find_median.Median
        self.Mole = find_mole.FindMole
        self.c = compute_ratio.PS2
        self.ps = p_s.PS
        self.p = 0
        self.s = 0
        self.label = 0
        self.median = [0, 0]
        self.mole = []
        self.ratio = 0

    def run(self):
        self.cls = clustering.Clustering(self.img)
        print('<|', end='', flush=True)
        self.img, self.label = self.cls.run()
        print('|', end='', flush=True)
        self.S = smoothing.Smooth(self.img, self.label, n=10)
        self.img = self.S.run()
        print('|', end='', flush=True)
        self.M = find_median.Median(self.img, self.label)
        self.median = self.M.run()
        print('|', end='', flush=True)
        self.Mole = find_mole.FindMole(self.img, self.median, self.label)
        self.mole = self.Mole.run()
        print('|', end='', flush=True)
        self.ps = p_s.PS(self.img, self.label, self.mole)
        self.p, self.s = self.ps.run()
        self.c = compute_ratio.PS2(self.p, self.s)
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
    img = matplotlib.image.imread([i for i in img.run()][1])
    obj = Run(img)
    obj.run()
    obj.show_images()
    print('Area : ', obj.s)
    print('Perimeter : ', obj.p)
    print('Ratio : ', obj.ratio)
