from unittest import TestCase
from nose.tools import eq_

import cv2
import numpy as np
import lib


class TestUtil(TestCase):
    """
    Test Case for basic module
    """

    def test_basic_search(self):
        img1 = cv2.imread("./test/img/taxio_mini.jpg")
        img2 = cv2.imread("./test/img/taxio.jpg")

        dst = lib.basic_search(img1, img2)
        eq_(dst.get('position'), (94, 200))
