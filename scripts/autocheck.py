import os
import pytesseract
import pyautogui

from PIL import Image

from .utils import keep_numerics

class AutoCheck(object):

    def __init__(self, img_path="./imgs"):

        self._zeny_icon = Image.open(_ZENY_)

    def get_all_price(self):
        """
        Get the all prices on the screen

        @return
            prices: [int]
        """
        # in order to skip the zeny icon

        results = []
        skip_width = self._zeny_icon.width

        targets = pyautogui.locateAllOnScreen(_zeny_icon)

        for x, y, _, _ in targets:
            img = self._capture_target(x+skip_width, y, 100, self._zeny_icon.height)
            price = recognize_price(img)

            if price is not None: results.append(price)

        return results

    def _capture_target(self, x, y, window_width, window_height):
        """
        Take a shot on x, y
        """
        return pyautogui.screenshot(region=(x, y, window_width, window_height))


    def _recognize_price(self, img):
        """
        use tesseract OCR to recognize digits

        @params
            img: given Image

        @return
            number: Int
        """
        # use the ro.traineddata
        tesseract_config = "-l ro"

        predict = pytesseract.image_to_string(img, config=tesseract_config)

        return keep_numerics(predict)
