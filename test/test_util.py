from unittest import TestCase
from nose.tools import eq_

import cv2
import numpy as np
import lib


class TestUtil(TestCase):
    """
    Test Case for util module
    """

    def test_is_same_image_type(self):

        img1 = cv2.imread("./test/img/taxio_mini.jpg", cv2.IMREAD_COLOR)
        img2 = cv2.imread("./test/img/taxio_mini.jpg", cv2.IMREAD_GRAYSCALE)
        img3 = cv2.imread("./test/img/vimlogo.png", cv2.IMREAD_COLOR)

        eq_(lib.is_same_image_type(img1, img2), False)
        eq_(lib.is_same_image_type(img1, img3), True)
        eq_(lib.is_same_image_type(img2, img3), False)
