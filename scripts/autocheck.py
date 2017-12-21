import os
import tesseract
import pyautogui as bot

from PIL import Image

class AutoCheck(object):

    def __init__(self, img_path="./imgs"):

        self._zeny_icon = Image.open(_ZENY_)

        pass

    def capture_price(self):
        """
        Get the all prices on the screen

        @return
            prices: [int]
        """
        pass

    def _find_coordinates(self, img):
        """
        Find the given image location

        @params
            img: given image

        @return
            coordinates: (x, y, width, height)
        """
        pass

    def _recognize_digits(self, img):
        """
        use tesseract OCR to recognize digits

        @params
            img: given Image

        @return
            number: Int
        """
        pass
