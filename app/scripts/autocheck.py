import os
import pytesseract
import pyautogui

from PIL import Image

from app.scripts.utils import keep_numerics
from app import config

class AutoCheck(object):

    def __init__(self):

        self._zeny_icon = Image.open(config.ZENY_ICON)

    def get_all_price(self):
        """
        Get the all prices on the screen

        @return
            prices: [int]
        """
        # in order to skip the zeny icon

        results = []
        skip_width = self._zeny_icon.width

        targets = pyautogui.locateAllOnScreen(self._zeny_icon)
        print(targets)
        for x, y, _, _ in targets:
            print(x, y)
            img = self._capture_target(x+skip_width, y, 100, self._zeny_icon.height)
            img.show()
            #price = self._recognize_price(img)
            #results.append(price)

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
