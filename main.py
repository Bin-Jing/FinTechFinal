
from reco import *
from seg import *
class Receipt:
    def __init__(self, Img):
        self.ImgName = Img
    def main(self):
        cutImg(self.ImgName)
        code = DeCode()
        print(code)

if __name__ == '__main__':
    r = Receipt("img.jpg")
    r.main()



