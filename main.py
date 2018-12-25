
from reco import *
from seg import *
from azure import *

key =""
class Receipt:
    def __init__(self, Img):
        self.ImgName = Img
    def main(self):
        cutImg(self.ImgName)
        code = DeCode()
        storeDate = StoreText(key)
        CashT = CashText(key)
        
        print(code)
        print(storeDate)
        print(CashT)


if __name__ == '__main__':
    r = Receipt("img.jpg")
    r.main()



