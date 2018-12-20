import cv2
import numpy as np
import skimage

def cutImg(name):

    img = cv2.imread(name)
    side = 1200
    ratio = float(side) / max(img.shape)
    img = skimage.img_as_ubyte(
                               skimage.transform.resize(
                                                        img, (int(img.shape[0] * ratio), int(img.shape[1] * ratio))))
    x = 300
    y = 0
    w = 300
    h = 1140

    raw_img = img[y:y+h, x:x+w]
#    cv2.imshow("raw", raw_img)
    cv2.imwrite('raw.jpg', raw_img)

    store_y = 0
    store_h = 60

    store_img = raw_img[store_y:store_y+store_h, 0:w]
    cv2.imwrite('store.jpg', store_img)

    date_y = store_h
    date_h = 50

    date_img = raw_img[date_y:date_y+date_h, 0:w]
    cv2.imwrite('date.jpg', date_img)

    code_y = date_y + date_h
    code_h = 120

    code_img = raw_img[code_y:code_y+code_h, 0:w]
    cv2.imwrite('code.jpg', code_img)
    
    codeEN_img = raw_img[code_y:code_y+code_h, 0:int(w/4)]
    cv2.imwrite('codeEN.jpg', codeEN_img)

    cash_y = code_y + code_h
    cash_h = 660

    cash_img = raw_img[cash_y:cash_y+cash_h, 0:w]
    cv2.imwrite('cash.jpg', cash_img)


