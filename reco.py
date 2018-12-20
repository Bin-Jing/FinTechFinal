import pytesseract
from PIL import Image
import cv2
import string

code = []
whitelist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def codeReco(name,threshold):
    img = Image.open(name);
    #image = cv2.imread('123.jpg')
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgry = img.convert("L")
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()
    text = pytesseract.image_to_string(out)
    new_s = ""
    for char in text:
        if char in whitelist:
            new_s += char
    else:
        new_s += ' '
    code.append(new_s)
#    print(text)
def DeCode():
    codeReco("1234.jpg",225)
    codeReco("2222.jpg",200)
    s = ''.join(code)
    print(s)

DeCode()
