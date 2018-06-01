import cv2
import numpy as np
import lib


if __name__ == "__main__":
    print("demo program")
    img1 = cv2.imread("./test/img/taxio_mini.jpg")
    img2 = cv2.imread("./test/img/taxio.jpg")

    print(lib.basic_search(img1, img2))
