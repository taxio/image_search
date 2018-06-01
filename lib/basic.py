import cv2
import numpy as np
from progressbar import ProgressBar

import lib


def basic_search(target_img: np.ndarray, from_img) -> dict:
    """
    :param target_img: 目的画像(この画像の位置を見つける)
    :param from_img: 検索対象画像(この画像から目的画像を見つける)
    :return: 目的画像が存在しそうな位置の候補．{position:(x,y), diff:float}のdictを返す．
    """

    if not lib.is_same_image_type(target_img, from_img):
        print("image type is different")
        return []

    tgt_size = target_img.shape[:2]
    frm_size = from_img.shape[:2]
    if tgt_size[0] > frm_size[0] or tgt_size[1] > frm_size[1]:
        print("target image is too large")
        return []

    size_diff = tuple(frm_size[i] - tgt_size[i] for i in range(2))
    diffs = list()
    pbar = ProgressBar(max_value=size_diff[0]*size_diff[1])
    for i in range(size_diff[0]):
        for j in range(size_diff[1]):
            diff = calc_pixcel_diff(target_img, from_img[i:i+tgt_size[0], j:j+tgt_size[1]])
            diffs.append({
                "position": (i, j),
                "diff": diff
            })
            pbar.update(i*size_diff[1]+j)
    pbar.finish()

    diffs.sort(key=lambda x:x["diff"])
    return diffs[0]


def calc_pixcel_diff(img1: np.ndarray, img2: np.ndarray) -> float:

    img_diff = np.abs(img2.astype(np.int32) - img1.astype(np.int32))
    diff = np.mean(img_diff)

    return diff