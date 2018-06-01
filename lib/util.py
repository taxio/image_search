import numpy as np


def is_same_image_type(img1: np.ndarray, img2: np.ndarray) -> bool:
    """
    画像の種類が同じかどうか
    :param img1: 対象画像1
    :param img2: 対象画像2
    :return: boolean
    """
    shape1 = img1.shape
    shape2 = img2.shape

    # color or gray
    if len(shape1) != len(shape2):
        return False

    # channels
    if len(shape1) == 3 and len(shape2) == 3:
        if shape1[2] != shape2[2]:
            return False

    return True

