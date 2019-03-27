import os


class OS:
    def __init__(self):
        os.chdir('Samples_images')
        self.images = []

    def read_images(self):
        self.images = os.listdir(os.getcwd())
        return self

    def run(self):
        self.read_images()
        yield from self.images
