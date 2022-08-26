from myselenium.getRoot import get_root


class TXTWriter(object):
    def __init__(self, filename):
        self.f = open(get_root() + filename, 'a')

    def write(self, word):
        self.f.write(word + "\n")

    def close(self):
        self.f.close()
