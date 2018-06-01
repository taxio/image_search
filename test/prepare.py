import cv2
import numpy as np


def to_gray(img_name: str, output_name: str):
    img = cv2.imread(img_name)
    if img is None:
        print("{} cannot find".format(img_name))
        return
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(output_name, gray)


if __name__ == "__main__":
    print("prepare program")
    # to_gray("./img/taxio_mini.jpg", "./img/taxio_mini_gray.png")
