import cv2 as cv

UPARROWCODE = 82
DOWNARROWCODE = 81

LEFTARROWCODE = 80
RIGHTARROWCODE = 79

parcours = ['C:\Users\jerem\PycharmProjects\carML\img\parcours_1.jpg',
            'C:\Users\jerem\PycharmProjects\carML\img\parcours_2.jpg',
            'C:\Users\jerem\PycharmProjects\carML\img\parcours_3.jpg']


def get_grid(img):
    im_gray = cv.imread(img, cv.IMREAD_GRAYSCALE)
    im_bw = cv.threshold(im_gray, 127, 255, cv.THRESH_BINARY)[1]
    return im_bw
