
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
        txtf = open("Output.txt", "w")
        txtf.write("{0}\n{1}\n{2}".format(code,storeDate,CashT))
        txtf.close()






