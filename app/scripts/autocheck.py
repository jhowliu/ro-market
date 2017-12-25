import os
import pytesseract
import pyautogui

from PIL import Image

from app import config

from app.scripts.utils import keep_numerics
from app.scripts.utils import FindCoordinates

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
        FindCoordinates.locate_target(config.ZENY_ICON)
        # middle points
        targets = FindCoordinates.locate_all_targets(config.ZENY_ICON)

        for x, y in targets:
            img = self._capture_target(x+skip_width+5, y, 100, self._zeny_icon.height)
            price = self._recognize_price(img)
            results.append(price)

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
        # check if os system is windows
        # use the ro.traineddata
        if os.name == 'nt':
            tesseract_config = "--tessdata-dir D:\Tesseract-OCR\\tessdata -l ro"
        else:
            tesseract_config = "-l ro"

        predict = pytesseract.image_to_string(img, config=tesseract_config)

        return keep_numerics(predict)
