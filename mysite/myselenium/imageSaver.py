import os

from myselenium.getRoot import get_root


class ImageSaver (object) :

    def __init__(self, img_path, locator):
        os.mkdir(get_root() + img_path)
        self.img_path = get_root() + img_path
        self.locator = locator

    def screenshot(self, name):
        self.locator.get_screenshot(name, self.img_path)
